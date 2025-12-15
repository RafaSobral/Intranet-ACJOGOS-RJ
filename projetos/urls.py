from django.urls import path
from . import views

app_name = 'projetos'

urlpatterns = [
    path('meus/', views.meus_projetos_view, name='meus_projetos'),
    path('criar/', views.criar_projeto_view, name='criar_projeto'),
    path('<int:pk>/', views.visualizar_projeto_view, name='visualizar_projeto'),
    path('<int:pk>/editar/', views.editar_projeto_view, name='editar_projeto'),
    path('<int:pk>/deletar/', views.deletar_projeto_view, name='deletar_projeto'),
]