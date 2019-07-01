"""info419livrosusados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core.views import index, cadLiv, excluir, login, registro, dados, generos, cadGen, livros, editar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('cadLiv/', cadLiv, name='cadLiv'),
    path('generos/', generos, name='generos'),
    path('cadGen/', cadGen, name='cadGen'),
    path('editar/<int:id>/', editar, name='editar'),
    path('excluir/<int:id>/', excluir, name="excluir"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('livros/<int:id>/', livros, name='livros'),
    path('registro/', registro, name='registro'),
    path('dados/<int:id>', dados, name='dados'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
