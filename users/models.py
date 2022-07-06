from email.policy import default
from pydoc import describe
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from pyparsing import null_debug_action
from pyrsistent import b
# Create your models here.


class User_profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile")
    phone = models.CharField(max_length=15, blank=True, null=True)
    mail = models.EmailField(max_length=254, blank=True, null=True)
    description = models.CharField(max_length=254, blank=True, null=True)
    website = models.URLField(max_length=254, blank=True, null=True)
    image = models.ImageField(
        upload_to="profile_image", blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfil de Usuarios'

    # def __str__(self):
    #     return self.user
