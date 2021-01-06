# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('versailles.apps.base.urls')),
    url(r'^login/', include('versailles.apps.login.urls')),
    url(r'^cadastro/', include('versailles.apps.cadastro.urls')),
    url(r'^fiscal/', include('versailles.apps.fiscal.urls')),
    url(r'^vendas/', include('versailles.apps.vendas.urls')),
    url(r'^compras/', include('versailles.apps.compras.urls')),
    url(r'^financeiro/', include('versailles.apps.financeiro.urls')),
    url(r'^estoque/', include('versailles.apps.estoque.urls')),
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
