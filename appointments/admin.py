from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "patient",
        "doctor",
        "appointment_date",
        "status",
    )

    search_fields = (
        "patient__username",
        "doctor__name",
    )

    list_filter = (
        "status",
        "appointment_date",
    )

    ordering = (
        "-appointment_date",
    )

    list_per_page = 10