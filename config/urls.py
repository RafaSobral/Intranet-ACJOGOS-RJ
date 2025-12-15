from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publico.urls', namespace='publico')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('empresas/', include('empresas.urls', namespace='empresas')),
    path('projetos/', include('projetos.urls', namespace='projetos')),
    path('pesquisas/', include('pesquisas.urls', namespace='pesquisas')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)