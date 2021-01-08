# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('djangoSIGE.apps.base.urls')),
    url(r'^login/', include('djangoSIGE.apps.login.urls')),
    url(r'^cadastro/', include('djangoSIGE.apps.cadastro.urls')),
    url(r'^fiscal/', include('djangoSIGE.apps.fiscal.urls')),
    url(r'^vendas/', include('djangoSIGE.apps.vendas.urls')),
    url(r'^compras/', include('djangoSIGE.apps.compras.urls')),
    url(r'^financeiro/', include('djangoSIGE.apps.financeiro.urls')),
    url(r'^estoque/', include('djangoSIGE.apps.estoque.urls')),
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
