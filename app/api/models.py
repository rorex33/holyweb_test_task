from django.db import models

class Client(models.Model):
    "Сущность клиента (он же пользователь)."
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    patronymic = models.CharField(max_length=256) # Отчество

# Отношение между сущностями "Doctor" и "Specialization"
# рассматриваем как один ко многим, принимая что один доктор
# может иметь лишь одну специализацию, а одна специализация
# может быть у многих докторов.

class Specialization(models.Model):
    "Сущность специализации доктора."
    title = models.CharField(max_length=256)

class Doctor(models.Model):
    "Сущность доктора."
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    patronymic = models.CharField(max_length=256) # Отчество

class Appointment(models.Model):
    "Сущность приёма у доктора."
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_at = models.DateTimeField(unique=True) # Дата и время встречи с врачём