from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "department",
        "specialization",
        "visiting_fee",
    )

    search_fields = (
        "name",
        "department",
        "specialization",
    )

    list_filter = (
        "department",
    )

    ordering = (
        "name",
    )

    list_per_page = 10