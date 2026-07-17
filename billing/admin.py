from django.contrib import admin
from .models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "patient",
        "doctor",
        "consultation_fee",
        "discount",
        "total_amount",
        "created_at",
    )

    search_fields = (
        "patient__username",
        "doctor__name",
    )

    list_filter = (
        "created_at",
        "doctor",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 10