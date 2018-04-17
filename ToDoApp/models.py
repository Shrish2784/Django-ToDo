from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class ToDo(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo'


class User_Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_photo = models.ImageField(upload_to = 'ToDoApp/ProfilePhotos')

    def __str__(self):
        return self.User.username

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

def createUserProfile(sender, **kwargs):
    if kwargs['created']:
        print(kwargs['instance'])
        user_profile = User_Profile.objects.create(User=kwargs['instance'])

post_save.connect(createUserProfile, sender=User)
