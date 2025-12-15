from django.urls import path
from . import views

app_name = 'pesquisas'

urlpatterns = [
    path('responder/<int:ano>/', views.responder_pesquisa_view, name='responder'),
    path('minhas/', views.minhas_pesquisas_view, name='minhas_pesquisas'),
]