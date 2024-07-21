from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
# positiveint = + number for age
# null is for saving blank space in DB and blank is for saving blank space in form
# abstractuser = username,lastname,firstname,email,password + age with customuser
