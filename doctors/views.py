from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["department"]

    search_fields = [
        "name",
        "specialization",
    ]

    ordering_fields = [
        "name",
        "visiting_fee",
    ]