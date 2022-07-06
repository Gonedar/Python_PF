from django.urls import path
from products.views import Lista_tortas, petitf, box, Cargar_torta, buscar_torta, Detalle_torta, Editar_torta, Borrar_torta

urlpatterns = [
    path('tortas/', Lista_tortas.as_view(), name='lista_tortas'),
    path('petitfours/', petitf, name='petitfours'),
    path('box/', box, name='box'),
    path('cargar-torta/', Cargar_torta.as_view(), name='cargar_torta'),
    path('buscar-torta/', buscar_torta, name='buscar_torta'),
    path('detalle-torta/<int:pk>/', Detalle_torta.as_view(), name='detalle_torta'),
    path('editar-torta/<int:pk>/', Editar_torta.as_view(), name='editar_torta'),
    path('borrar-torta/<int:pk>/', Borrar_torta.as_view(), name='borrar_torta'),
]
