from django.db import models
from django.urls import reverse


# Create your models here.
class Volunteer(models.Model):
    id_dobrovolnik = models.AutoField(primary_key=True)
    meno = models.CharField(max_length=255)
    priezvisko = models.CharField(max_length=255)
    datum_narodenia = models.DateField()
    doveryhodnost = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse("volunteer_edit:volunteer-detail", kwargs={"id": self.id_dobrovolnik})
    
    class Meta:
        managed = False
        db_table = 'Dobrovolnik'


class Caregiver(models.Model):
    id_pecovatel = models.AutoField(primary_key=True)
    meno = models.CharField(max_length=255)
    priezvisko = models.CharField(max_length=255)
    datum_narodenia = models.DateField()
    
    def get_absolute_url(self):
        return reverse("caregiver_edit:caregiver-detail", kwargs={"id": self.id_pecovatel}) #f"/products/{self.id}/"

    class Meta:
        managed = False
        db_table = 'Pecovatel'


class VetRequest(models.Model):
    id_poziadavky = models.AutoField(primary_key=True)
    datum_vytvorenia = models.DateField()
    obsah = models.CharField(max_length=255)
    stav = models.CharField(max_length=255)
    pecovatelid = models.ForeignKey('Caregiver', models.DO_NOTHING, db_column='PecovatelID')
    veterinarid = models.ForeignKey('Vet', models.DO_NOTHING, db_column='VeterinarID')
    zvieraid = models.ForeignKey('Animal', models.DO_NOTHING, db_column='ZvieraID')

    class Meta:
        managed = False
        db_table = 'Poziadavka'


class Reservation(models.Model):
    id_rezervacie = models.AutoField(primary_key=True)
    datum_vytvorenia = models.DateField()
    rezervovany_od = models.DateField()
    rezervovany_do = models.DateField()
    schvalenie = models.IntegerField(blank=True, null=True)
    stav = models.CharField(max_length=255, blank=True, null=True)
    zvieraid = models.ForeignKey('Animal', models.DO_NOTHING, db_column='ZvieraID')
    dobrovolnikid = models.ForeignKey('Volunteer', models.DO_NOTHING, db_column='DobrovolnikID')
    
    def get_absolute_url(self):
        return reverse("reservation:reservation-detail", kwargs={"id": self.id_rezervacie}) #f"/products/{self.id}/"
    
    class Meta:
        managed = False
        db_table = 'Rezervacia'


class User(models.Model):
    id_uzivatel = models.AutoField(primary_key=True)
    typ = models.CharField(max_length=11)
    email = models.CharField(unique=True, max_length=255, db_collation='utf8mb4_unicode_520_ci')
    heslo = models.CharField(max_length=255, db_collation='utf8mb4_unicode_520_ci')
    aktivni = models.IntegerField()
    zamestnanec_id = models.PositiveIntegerField(blank=True, null=True)
    klient_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Uzivatel'


class Walk(models.Model):
    id_vencenia = models.AutoField(primary_key=True)
    venceny_od = models.DateField()
    venceny_do = models.DateField()

    class Meta:
        managed = False
        db_table = 'Vencenie'


class Vet(models.Model):
    id_veterinar = models.AutoField(primary_key=True)
    meno = models.CharField(max_length=255)
    priezvisko = models.CharField(max_length=255)
    datum_narodenia = models.DateField()

    class Meta:
        managed = False
        db_table = 'Veterinar'


class Animal(models.Model):
    id_zviera = models.AutoField(primary_key=True)
    druh = models.CharField(max_length=255)
    meno = models.CharField(max_length=255)
    vek = models.PositiveIntegerField()
    datum_registracie = models.DateField()
    obrazok = models.CharField(max_length=255, db_collation='utf8mb4_unicode_520_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Zviera'
    
    def get_absolute_url(self):
        return reverse("animals:animal-detail", kwargs={"id": self.id_zviera})
