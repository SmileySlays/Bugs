from django.db import models
from django.contrib.auth.models import AbstractUser

class MyCustomUser(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    