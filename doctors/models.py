    
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="doctor",
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    visiting_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name