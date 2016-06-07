from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Attendance(models.Model):
    user = models.ForeignKey(User)
    course_code = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=200, blank=True)
    classes = models.CharField(max_length=10, blank=True)
    attended = models.CharField(max_length=10, blank=True)
    absent = models.CharField(max_length=10, blank=True)
    percent = models.CharField(max_length=10, blank=True)
    updated = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.name


class Gpalist(models.Model):
    user = models.ForeignKey(User)
    sem = models.CharField(max_length=100)
    gpa = models.CharField(max_length=50)

    def __unicode__(self):
        return self.sem


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    regno = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)

    def __unicode__(self):
        return self.user.username
