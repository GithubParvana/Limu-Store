from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from PIL import Image

# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = (

        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    )

    bio = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='user_profile', null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=3, null=True, blank=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    website = models.URLField(max_length=255, null=True, blank=True)


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    

    def __str__(self):
        return self.username

    
    