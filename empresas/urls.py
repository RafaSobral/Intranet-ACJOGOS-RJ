from django.urls import path
from . import views

app_name = 'empresas'  # ← Precisa ter isso!

urlpatterns = [
    path('minhas/', views.minhas_empresas_view, name='minhas_empresas'),
    path('criar/', views.criar_empresa_view, name='criar_empresa'),
    path('<int:pk>/', views.visualizar_empresa_view, name='visualizar_empresa'),
    path('<int:pk>/editar/', views.editar_empresa_view, name='editar_empresa'),
    path('<int:pk>/deletar/', views.deletar_empresa_view, name='deletar_empresa'),
    path('<int:pk>/membros/', views.gerenciar_membros_view, name='gerenciar_membros'),
]