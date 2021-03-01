from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fondo = models.CharField(max_length=150)
    letra = models.CharField(max_length=150)
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('profile_detail', args=[str(self.id)])