from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


def get_absolute_url(self):
    return reverse("caregiver_edit:caregiver-detail", kwargs={"id": self.id})

User.add_to_class('get_absolute_url', get_absolute_url)
