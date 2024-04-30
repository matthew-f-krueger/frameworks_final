from django.urls import path
from animal_adoption_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
