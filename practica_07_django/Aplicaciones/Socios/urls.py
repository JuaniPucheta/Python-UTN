from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarSocio/', views.registrarSocio),
    path('edicionSocio/<str:dni>', views.edicionSocio),
    path('editarSocio/', views.editarSocio),
    path('eliminarSocio/<str:dni>', views.eliminarSocio),
]