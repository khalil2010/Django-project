"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from peinture import views
from peinture.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.couleur_search,name='accueil'),
    path('couleur_search/',views.couleur_search,name='search'),
    path('login_view/',views.login_view,name="login_view"),
    path('couleur_list/',views.couleur_list, name="couleur_list"),
    path('couleur/<str:couleur_id>/update/', views.couleur_update, name='couleur_update'),
    path('couleur/<str:couleur_id>/delete/', views.couleur_delete, name='couleur_delete'),
    path('couleur/add/', views.add_couleur, name='add_couleur'),
    path('', views.formules_couleurs, name='formules_couleurs'),
     path('couleur/<int:couleur_id>/', views.couleur_details, name='couleur_details'),
    
]
