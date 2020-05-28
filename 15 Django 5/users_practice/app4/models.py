from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):

    admi = models.OneToOneField(User,on_delete=models.CASCADE)  #Since Django 2.x on_delete is required. In older versions it defaults to CASCADE
    # This is adding users to the Users field in Django Administration page not adding users to app users

    website = models.URLField(blank=True) #remember to give same field name in forms.py
    profile_pic = models.ImageField(upload_to = 'profile_folder', blank=True)

    def __str__(self):
        return self.admi.username
