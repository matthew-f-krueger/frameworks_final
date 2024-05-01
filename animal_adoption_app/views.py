from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal

def index(request):
    # return HttpResponse("Hello World!")
    my_dict={'insert_me': 'Cats are cool and stuff'}
    return render(request, 'animal_adoption_app/index.html', context=my_dict)

def foster_list(request):
    foster_list = Animal.objects.filter(fosterable=True)
    return render(request, 'animal_adoption_app/foster.html', {'foster_list': foster_list})

def adopt_list(request):
    adoption_list = Animal.objects.filter(fosterable=False)
    return render(request, 'animal_adoption_app/adopt.html', {'adoption_list': adoption_list})