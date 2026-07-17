from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=150)
    phone = models.CharField(
        max_length=20,
        unique=True
    )
    address = models.TextField()

    def __str__(self):
        return self.user.username