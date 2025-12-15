from django.urls import path
from . import views

app_name = 'publico'  # ← Esta linha é OBRIGATÓRIA quando usa namespace

urlpatterns = [
    path('', views.home_view, name='home'),
    path('empresas/', views.empresas_list_view, name='empresas'),
    path('projetos/', views.projetos_list_view, name='projetos'),
    path('mapa/', views.mapa_view, name='mapa'),
]