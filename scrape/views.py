from django.shortcuts import render
from scrape.models import Attendance, Gpalist, UserProfile
from scrape.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import mechanize
import cookielib
from bs4 import BeautifulSoup as BS
import os
import sys
# Create your views here.

# Index


def index(request):
    return render(request, 'scrape/index.html')


# Display Attendance

def show_atd(request):
    user = request.user
    try:
        atx = Attendance.objects.filter(user=user)
        context_dict = {'atx': atx}
    except Attendance.DoesNotExist:
        pass
    return render(request, 'scrape/atx.html', context_dict)
# Register new user


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context_dict = {'user_form': user_form,
                    'profile_form': profile_form, 'registered': registered}
    return render(request, 'scrape/register.html', context_dict)


# Login

def user_login(request):
    context_dict = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/scrape/atd')
            else:
                context_dict['disabled_account'] = True
                return render(request, 'scrape/login.html', context_dict)
        else:
            print "Invalid login details: {0},{1}".format(username, password)
            context_dict['bad_details'] = True
            return render(request, 'scrape/login.html', context_dict)
    else:
        return render(request, 'scrape/login.html', context_dict)

# Logout


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/scrape/')


@login_required
def get_atd(request):
    user = request.user
    up=UserProfile.objects.get(user=user)
    reload(sys)
    sys.setdefaultencoding("utf8")

    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    # br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    br.addheaders = [('User-agent', 'Chrome')]
    reg = up.regno
    bd = up.dob
    pg = br.open('http://websismit.manipal.edu/')

    br.select_form(name='loginform')

    # user Credentials
    br.form['idValue'] = reg
    br.form['birthDate_i18n'] = bd
    br.form['birthDate'] = bd
    br.submit()

    response = br.response()
    # print response.info()
    for link in br.links():
        if link.text == 'Academic Status':
            lk = link
            break
    for link in br.links():
        if link.text == 'EXIT':
            logout = link
            break

    # print lk.text
    reqs = br.click_link(lk)
    resp = br.follow_link(lk)
    soup = BS(resp.read())

    als = soup.findAll('a')
    for al in als:
        if al.get('title') == 'Latest Enrollment':
            ur = al.get('href')
    br.find_link(url=ur)
    req = br.click_link(url=ur)
    res = br.open(req)
    soup = BS(res.read())

    table = soup.find('table', id='ListAttendanceSummary_table')
    rows = table.findAll('tr')
    data = [[td.findChildren(text=True)
             for td in tr.findAll("td")] for tr in rows]
    data = [[u"".join(d).strip() for d in l] for l in data]
    iterdata = iter(data)
    next(iterdata)
    for d in iterdata:
        try:
            a = Attendance.objects.get(user=user, name=d[1])
        except Attendance.DoesNotExist:
            a=None
            pass
        if a:
            a.classes=d[2]
            a.attended=d[3]
            a.absent=d[4]
            a.percent=d[5]
            a.updated=d[6]
        else:
            a = Attendance(user=user, course_code=d[0], name=d[1], classes=d[
                           2], attended=d[3], absent=d[4], percent=d[5], updated=d[6])
        a.save()
    return HttpResponseRedirect('/scrape/atx')
