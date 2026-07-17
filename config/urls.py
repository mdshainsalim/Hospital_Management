from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hospital Management System API is Running")


urlpatterns = [
    path('', home),   # <-- Add this line
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path("api/", include("doctors.urls")),
    path("api/", include("appointments.urls")),
    path("api/", include("billing.urls")),
    path("api/dashboard/", include("dashboard.urls")),
]