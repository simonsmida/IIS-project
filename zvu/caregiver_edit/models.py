from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


def get_absolute_url(self):
    return reverse("caregiver_edit:caregiver-detail", kwargs={"id": self.id})

User.add_to_class('get_absolute_url', get_absolute_url)
# Create your models here.

# class Caregiver(models.Model):
#     id_pecovatel = models.AutoField(primary_key=True)
#     meno = models.CharField(max_length=255)
#     priezvisko = models.CharField(max_length=255)
#     datum_narodenia = models.DateField()

#     # class Meta:
#     #     managed = False
#     #     db_table = 'Pecovatel'

#     def get_absolute_url(self):
#         return reverse("caregiver_edit:caregiver-detail", kwargs={"id": self.id_pecovatel}) #f"/products/{self.id}/"