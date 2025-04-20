from django.contrib import admin

from .models import Client, Doctor, Specialization, Appointment

admin.site.register(Client)
admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Appointment)
