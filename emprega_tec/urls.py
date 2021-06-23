"""emprega_tec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.conf import settings
from core import views

urlpatterns = [
    path('', RedirectView.as_view(url='/index/')),
    path('admin/', admin.site.urls),
    path('index/', views.principal, name='principal'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/delete', views.delete_vaga, name='delete_vaga'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('vagas/', views.vagas, name='vagas'),
    path('vagas/submit', views.candidatura, name='candidatura'),
    path('perfil/submit', views.nova_vaga, name='nova_vaga'),
    path('login/', views.login_usuario, name='login'),
    path('login/submit', views.submit_login, name='submit_login'),
    path('logout/', views.logout_user),
    path('cadastro_candidato/', views.cadastro_candidato, name='cadastro_candidato'),
    path('cadastro_candidato/submit', views.cadastrar_candidato, name='cadastrar_candidato'),
    path('cadastro_empresa/', views.cadastro_empresa, name='cadastro_empresa'),
    path('cadastro_empresa/submit', views.cadastrar_empresa, name='cadastrar_empresa'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

