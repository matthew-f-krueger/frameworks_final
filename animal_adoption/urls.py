"""
URL configuration for animal_adoption project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from animal_adoption_app import views
from django.conf.urls import include

urlpatterns = [
    path('', include('animal_adoption_app.urls')),
    path('admin/', admin.site.urls),
    
    path('foster/', views.foster_list, name='foster_list'),
    path('adopt/', views.adopt_list, name='adopt_list'),

    path('animal/<int:animal_id>/', views.animal_detail_view, name='animal_detail'),

    path('dogs/', views.dogs, name='dogs'),
    path('cats/', views.cats, name='cats'),
    path('lizards/', views.lizards, name='lizards'),
    path('birds/', views.birds, name='birds'),
    path('fish/', views.fish, name='fish'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('homeward/', views.homeward, name='homeward'),
    path('cats-cradle/', views.cats_cradle, name='cats_cradle'),
    path('minn-kota/', views.minn_kota, name='minn_kota'),

    path('filter-adopt/', views.filter_adopt, name='filter_adopt'),
    path('filter-foster/', views.filter_foster, name='filter_foster'),

    path('filter_homeward/', views.filter_homeward, name='filter_homeward'),
    path('filter_cats_cradle/', views.filter_cats_cradle, name='filter_cats_cradle'),
    path('filter_minn_kota/', views.filter_minn_kota, name='filter_minn_kota'),

    path('all-animals/', views.all_animals, name='all_animals'),
]
