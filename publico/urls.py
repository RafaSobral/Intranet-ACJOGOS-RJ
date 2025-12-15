from django.urls import path
from . import views

app_name = 'publico'

urlpatterns = [
    # Página inicial
    path('', views.home_view, name='home'),
    
    # Listagens públicas
    path('empresas/', views.empresas_list_view, name='empresas'),
    path('empresas/<int:pk>/', views.empresa_detail_view, name='empresa_detail'),
    
    path('projetos/', views.projetos_list_view, name='projetos'),
    path('projetos/<int:pk>/', views.projeto_detail_view, name='projeto_detail'),
    
    # Mapa interativo
    path('mapa/', views.mapa_view, name='mapa'),
    
    # API para dados do mapa (JSON)
    path('api/empresas-mapa/', views.empresas_mapa_json, name='empresas_mapa_json'),
]