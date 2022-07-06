from distutils.command.upload import upload
from turtle import up
from unicodedata import name
from django.db import models

# Create your models here.


class Tortas(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    weight = models.FloatField(max_length=3, blank=True, null=True)
    price = models.FloatField(max_length=3, blank=True, null=True)
    SKU = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="tortas", blank=True, null=True)

    class Meta:
        verbose_name = "Torta"
        verbose_name_plural = "Tortas"

    def __str__(self):
        return self.name


class Petitfours(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    unit = models.FloatField(max_length=3, blank=True, null=True)
    price = models.FloatField(max_length=3, blank=True, null=True)
    SKU = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Petit Four"
        verbose_name_plural = "Petit Fours"


class Box(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    ingredients = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(max_length=3, blank=True, null=True)
    SKU = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Box"
        verbose_name_plural = "Boxes"
