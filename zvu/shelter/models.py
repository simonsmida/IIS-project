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
    
    def get_absolute_url(self):
        return reverse("vetrequest:vetrequest-detail", kwargs={"id": self.id})

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField()
    reserved_from = models.DateField()
    reserved_to = models.DateField()
    approval = models.IntegerField(default=0)
    state = models.CharField(max_length=255, default='pending')
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
    image = models.CharField(max_length=255, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("animals:animal-detail", kwargs={"id": self.id})


# Create your models here.
# class Volunteer(models.Model):
#     id = models.AutoField(primary_key=True)
#     meno = models.CharField(max_length=255)
#     priezvisko = models.CharField(max_length=255)
#     datum_narodenia = models.DateField()
#     doveryhodnost = models.IntegerField()
    
#     def get_absolute_url(self):
#         return reverse("volunteer_edit:volunteer-detail", kwargs={"id": self.id})
    

# class Caregiver(models.Model):
#     id = models.AutoField(primary_key=True)
#     meno = models.CharField(max_length=255)
#     priezvisko = models.CharField(max_length=255)
#     datum_narodenia = models.DateField()
    
#     def get_absolute_url(self):
#         return reverse("caregiver_edit:caregiver-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"


# class User(models.Model):
#     id_uzivatel = models.AutoField(primary_key=True)
#     typ = models.CharField(max_length=11)
#     email = models.CharField(unique=True, max_length=255, db_collation='utf8mb4_unicode_520_ci')
#     heslo = models.CharField(max_length=255, db_collation='utf8mb4_unicode_520_ci')
#     aktivni = models.IntegerField()
#     zamestnanec_id = models.PositiveIntegerField(blank=True, null=True)
#     klient_id = models.PositiveIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Uzivatel'


# class Walk(models.Model):
#     id_vencenia = models.AutoField(primary_key=True)
#     venceny_od = models.DateField()
#     venceny_do = models.DateField()


# class Vet(models.Model):
#     id_veterinar = models.AutoField(primary_key=True)
#     meno = models.CharField(max_length=255)
#     priezvisko = models.CharField(max_length=255)
#     datum_narodenia = models.DateField()
