from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Bill


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(request):

    data = {
        "total_patients": User.objects.filter(is_staff=False).count(),
        "total_doctors": Doctor.objects.count(),
        "total_appointments": Appointment.objects.count(),

        "pending": Appointment.objects.filter(
            status="Pending"
        ).count(),

        "confirmed": Appointment.objects.filter(
            status="Confirmed"
        ).count(),

        "completed": Appointment.objects.filter(
            status="Completed"
        ).count(),

        "cancelled": Appointment.objects.filter(
            status="Cancelled"
        ).count(),

        "total_bills": Bill.objects.count(),
    }

    return Response(data)