from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Animal, Dog, Cat, Lizard, Bird, Fish

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


def animal_detail_view(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if hasattr(animal, 'dog'):
        animal_type = 'Dog'
        animal_info = get_object_or_404(Dog, animal=animal)
    elif hasattr(animal, 'cat'):
        animal_type = 'Cat'
        animal_info = get_object_or_404(Cat, animal=animal)
    elif hasattr(animal, 'lizard'):
        animal_type = 'Lizard'
        animal_info = get_object_or_404(Lizard, animal=animal)
    elif hasattr(animal, 'bird'):
        animal_type = 'Bird'
        animal_info = get_object_or_404(Bird, animal=animal)
    elif hasattr(animal, 'fish'):
        animal_type = 'Fish'
        animal_info = get_object_or_404(Fish, animal=animal)
    else:
        animal_type = 'Unknown'
        animal_info = None

    return render(request, 'animal_detail.html', {'animal': animal, 'animal_type': animal_type, 'animal_info': animal_info})
