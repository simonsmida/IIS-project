from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


def get_absolute_url(self):
    if self.groups.filter(name='caregiver').exists():
        type = 'caregiver'
    if self.groups.filter(name='volunteer').exists() or self.groups.filter(name='volunteer_notrust').exists():
        type = 'volunteer'
    if self.groups.filter(name='vet').exists():
        type = 'vet'
    return reverse(f"{type}_edit:{type}-detail", kwargs={"id": self.id})

User.add_to_class('get_absolute_url', get_absolute_url)
