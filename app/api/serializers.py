from rest_framework import serializers
from .models import *
import re

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'title']

class DoctorSerializer(serializers.ModelSerializer):
    specialization = serializers.CharField(source='specialization.title')
    class Meta:
        model = Doctor
        fields = ['name', 'surname', 'patronymic', 'specialization']

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_fullname = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['id', 'doctor_fullname', 'date', 'time']

    def get_doctor_fullname(self, obj):
        return f"{obj.doctor.surname} {obj.doctor.name} {obj.doctor.patronymic}"

    def get_date(self, obj):
        return obj.start_at.date()

    def get_time(self, obj):
        return obj.start_at.time()

class CreateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'start_at']

    def validate(self, data):
        return data