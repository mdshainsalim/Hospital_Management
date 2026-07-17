from django.db import models
from django.contrib.auth.models import User

from doctors.models import Doctor
from appointments.models import Appointment


class Bill(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bills"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="bills"
    )

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="bill"
    )

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    discount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.consultation_fee - self.discount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.id}"