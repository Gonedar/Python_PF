from django.contrib import admin
from products.models import Tortas, Petitfours, Box

# Register your models here.


@admin.register(Tortas)
class TortasAdmin(admin.ModelAdmin):
    list_display = ["SKU", "name", "price", "is_active"]


@admin.register(Petitfours)
class PetitfoursAdmin(admin.ModelAdmin):
    list_display = ["SKU", "name", "price", "is_active"]


# @admin.register(Box)
# class BoxAdmin(admin.ModelAdmin):
#     list_display = ["SKU", "name", "price", "is_active"]
