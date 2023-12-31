from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    school_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    class_name = models.CharField(max_length=20)

    def __str__(self):
        return self.username