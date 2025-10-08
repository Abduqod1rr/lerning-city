from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser,models.Model):
    ROLE_CHOICES=[
        ("Teacher","teacher"),
        ("Student","student"),
    ]
    
    role=models.CharField(choices=ROLE_CHOICES, max_length=50,default="Student")

    def __str__(self):
        return self.username