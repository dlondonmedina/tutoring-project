from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()
    dob = models.DateField()
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

