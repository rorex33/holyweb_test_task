from django.urls import path
from . import views

urlpatterns = [ 
    path("doctors/", views.get_doctors, name="doctors"),
    path("appointments/", views.get_appointments, name="appointments"),
    path("appointments/create/", views.create_appointment, name="appointment_create"),
]