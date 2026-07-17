from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated


from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):

    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "status",
        "doctor",
    ]

    search_fields = [
        "patient__username",
        "doctor__name",
    ]

    ordering_fields = [
        "appointment_date",
        "appointment_time",
    ]

    def get_queryset(self):
        user = self.request.user

        # Admin can see everything
        if user.is_superuser:
            return Appointment.objects.all()

        # Doctor can see only assigned appointments
        if hasattr(user, "doctor"):
            return Appointment.objects.filter(doctor=user.doctor)

        # Patient can see only their own appointments
        return Appointment.objects.filter(patient=user)

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)