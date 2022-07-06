from calendar import c
from re import template
import re
from socket import create_server
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from matplotlib import image
from products.models import Tortas, Petitfours, Box
from products.forms import Torta_form

# Create your views here.


class Lista_tortas(ListView):
    model = Tortas
    template_name = "tortas.html"
    queryset = Tortas.objects.filter(is_active=True)


class Detalle_torta(DetailView):
    model = Tortas
    template_name = "detalle_torta.html"
    fields = ["description", "weight", "price", "image"]


class Cargar_torta(LoginRequiredMixin, CreateView):
    model = Tortas
    template_name = "cargar_torta.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("detalle_torta", kwargs={"pk": self.object.pk})


class Editar_torta(LoginRequiredMixin, UpdateView):
    model = Tortas
    template_name = "editar_torta.html"
    fields = ["description", "weight", "price", "is_active", "image"]

    def get_success_url(self):
        return reverse("detalle_torta", kwargs={"pk": self.object.pk})


class Borrar_torta(LoginRequiredMixin, DeleteView):
    model = Tortas
    template_name = "borrar_torta.html"

    def get_success_url(self):
        return reverse("lista_tortas")


def buscar_torta(request):
    torta_busqueda = request.GET["search"]
    tortas = Tortas.objects.filter(name__icontains=torta_busqueda)
    if tortas.exists():
        context = {"tortas": tortas}
    else:
        context = {
            "errors": f"Te pedimos disculpas, pero no encontramos la torta: {torta_busqueda}"}
    return render(request, 'buscar_torta.html', context=context)


def petitf(request):
    petitf = Petitfours.objects.all()
    context = {"petitf": petitf}
    return render(request, 'petitfours.html', context=context)


def box(request):
    box = Box.objects.all()
    context = {"box": box}
    return render(request, 'box.html', context=context)
