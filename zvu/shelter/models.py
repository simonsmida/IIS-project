from django.db import models
from django.urls import reverse
from django.conf import settings


class Vetrequest(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField()
    content = models.CharField(max_length=255)
    state = models.CharField(max_length=255, default='pending')
    caregiverid = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='caregiver_req',
                                    db_column='CaregiverID')
    vetid = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE,related_name='vet_req',
                                    db_column='VetID')
    animalid = models.ForeignKey('Animal', models.CASCADE, db_column='AnimalID')
    exam_time = models.DateField()
    exam_procedure = models.CharField(max_length=255)
    exam_protocol = models.CharField(max_length=255)
    
    def get_absolute_url(self):
        return reverse("vetrequest:vetrequest-detail", kwargs={"id": self.id})

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    reserved_date = models.DateField()  
    reserved_from = models.TimeField()
    reserved_to = models.TimeField()
    approval = models.IntegerField(default=0)
    state = models.CharField(max_length=255, default='pending')
    time_picked = models.TimeField(blank=True, null=True)
    time_return = models.TimeField(blank=True, null=True)
    animalid = models.ForeignKey('Animal', models.CASCADE, db_column='AnimalID')
    volunteerid = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='VolunteerID')
    
    def get_absolute_url(self):
        return reverse("reservation:reservation-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"
   

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    breed = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    registration_date = models.DateField()
    info = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    health_record = models.CharField(max_length=255)
    
    def get_absolute_url(self):
        return reverse("animals:animal-detail", kwargs={"id": self.id})

class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    reserved_date = models.DateField()
    reserved_from = models.TimeField()
    reserved_to = models.TimeField()
    is_free = models.PositiveIntegerField(default=1)
    animalid = models.ForeignKey('Animal', models.CASCADE, db_column='AnimalID')
    
    def get_absolute_url(self):
        return reverse("timetable:timetable-update", kwargs={"id": self.id})

