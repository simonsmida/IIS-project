from django.db import models
from shelter.models import Pecovatel
from django.urls import reverse
# Create your models here.

class Caregiver(models.Model):
    id_pecovatel = models.AutoField(primary_key=True)
    meno = models.CharField(max_length=255)
    priezvisko = models.CharField(max_length=255)
    datum_narodenia = models.DateField()

    # class Meta:
    #     managed = False
    #     db_table = 'Pecovatel'

    def get_absolute_url(self):
        return reverse("caregiver:caregiver-detail", kwargs={"id": self.id_pecovatel}) #f"/products/{self.id}/"