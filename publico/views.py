from django.urls import path
from django.http import HttpResponse

app_name = 'publico'

# View temporária só para testar
def home_view(request):
    return HttpResponse("Bem-vindo à ACJOGOS-RJ!")

urlpatterns = [
    path('', home_view, name='home'),
]