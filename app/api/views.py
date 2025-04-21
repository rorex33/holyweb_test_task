from django.utils import timezone
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, time as dt_time, timedelta
from .serializers import *
from .models import *

@api_view(['GET'])
def get_doctors(request):
    doctors = Doctor.objects.select_related('specialization').all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_appointments(request):
    fullname = request.query_params.get('client_fullname', '').strip()
    if not fullname:
        return Response({'error': 'client_fullname parameter is required'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Разбиваем ФИО на части
    parts = re.split(r'\s+', fullname)
    if len(parts) < 2:
        return Response({'error': 'Invalid fullname format'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Ищем клиента по разным комбинациям ФИО
    query = Q()
    if len(parts) == 2:
        query |= Q(surname__iexact=parts[0], name__iexact=parts[1])
        query |= Q(name__iexact=parts[0], surname__iexact=parts[1])
    else:
        query |= Q(surname__iexact=parts[0], name__iexact=parts[1], patronymic__iexact=parts[2])
        query |= Q(name__iexact=parts[0], surname__iexact=parts[1], patronymic__iexact=parts[2])

    try:
        client = Client.objects.get(query)
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, 
                       status=status.HTTP_404_NOT_FOUND)

    appointments = Appointment.objects.filter(client=client).select_related('doctor')
    serializer = AppointmentSerializer(appointments, many=True)
    return Response({'data': serializer.data})

@api_view(['POST'])
def create_appointment(request):
    fullname = request.query_params.get('client_fullname', '').strip()
    if not fullname:
        return Response({'error': 'client_fullname parameter is required'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Разбираем тело запроса
    try:
        doctor_id = request.data.get('doctor_id')
        date_str = request.data.get('date')
        time_str = request.data.get('time')
        
        if not all([doctor_id, date_str, time_str]):
            return Response({'error': 'doctor_id, date and time are required'}, 
                          status=status.HTTP_400_BAD_REQUEST)

        # Парсим дату и время
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            time_obj = datetime.strptime(time_str, '%H:%M').time()
            start_at = timezone.make_aware(datetime.combine(date, time_obj))
        except ValueError:
            return Response({'error': 'Invalid date or time format'}, 
                        status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': 'Invalid request data'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Проверка на прошедшую дату
    if start_at < timezone.now():
        return Response({'error': 'appointment to past'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Проверка дня недели
    if start_at.weekday() >= 5:  # 5 и 6 - суббота и воскресенье
        return Response({'error': 'bad day of week'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Проверка рабочего времени
    if not (dt_time(9, 0) <= time_obj <= dt_time(18, 0)):
        return Response({'error': 'bad time - now work in this time'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Проверка длительности приём
    end_at = start_at + timedelta(hours=1)
    if end_at.time() > dt_time(18, 0):
        return Response({'error': 'bad time - duration limit exceeded'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Проверка существования доктора
    try:
        doctor = Doctor.objects.get(pk=doctor_id)
    except Doctor.DoesNotExist:
        return Response({'error': 'doctor not found'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Проверка занятости доктора
    if Appointment.objects.filter(
        doctor=doctor,
        start_at__range=(start_at, end_at - timedelta(minutes=1))
    ).exists():
        return Response({'error': 'doctor is busy'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Разбираем ФИО клиента
    parts = re.split(r'\s+', fullname)
    if len(parts) < 2:
        return Response({'error': 'Invalid fullname format'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Создаём или находим клиента
    if len(parts) == 2:
        client, created = Client.objects.get_or_create(
            surname=parts[0],
            name=parts[1],
            defaults={'patronymic': ''}
        )
    else:
        client, created = Client.objects.get_or_create(
            surname=parts[0],
            name=parts[1],
            patronymic=parts[2]
        )

    # Проверка на дублирование приёма
    if Appointment.objects.filter(start_at=start_at, doctor=doctor).exists():
        return Response({'error': 'duplicate'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Проверка что у клиента нет другого приёма в это время
    if Appointment.objects.filter(
        client=client,
        start_at__range=(start_at, end_at - timedelta(minutes=1))
    ).exists():
        return Response({'error': 'client have another appointment to this time'}, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Создаём приём
    appointment = Appointment.objects.create(
        client=client,
        doctor=doctor,
        start_at=start_at
    )

    return Response({'success': 'appointment created'}, 
                   status=status.HTTP_200_OK)