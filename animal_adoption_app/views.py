from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, Dog, Cat, Lizard, Bird, Fish
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def index(request):
    my_dict={'insert_me': 'Cats are cool and stuff'}
    return render(request, 'animal_adoption_app/index.html', context=my_dict)

def foster_list(request):
    foster_list = Animal.objects.filter(fosterable=True)
    return render(request, 'animal_adoption_app/foster.html', {'foster_list': foster_list})

def adopt_list(request):
    adoption_list = Animal.objects.filter(fosterable=False)
    return render(request, 'animal_adoption_app/adopt.html', {'adoption_list': adoption_list})

def dogs(request):
    dogs = Dog.objects.all()
    return render(request, 'animal_adoption_app/dogs.html', {'dog_list': dogs}) 

def cats(request):
    cats = Cat.objects.all()
    return render(request, 'animal_adoption_app/cats.html', {'cat_list': cats})

def lizards(request):
    lizards = Lizard.objects.all()
    return render(request, 'animal_adoption_app/lizards.html', {'lizard_list': lizards})

def birds(request):
    birds = Bird.objects.all()
    return render(request, 'animal_adoption_app/birds.html', {'bird_list': birds})

def fish(request):
    fish = Fish.objects.all()
    return render(request, 'animal_adoption_app/fish.html', {'fish_list': fish})

def homeward(request):
    homeward_animals = Animal.objects.filter(shelter='Homeward Animal Shelter')
    return render(request, 'animal_adoption_app/homeward.html', {'homeward_animals': homeward_animals})

def cats_cradle(request):
    cats_cradle_animals = Animal.objects.filter(shelter='Cats Cradle Shelter Inc')
    return render(request, 'animal_adoption_app/cats_cradle.html', {'cats_cradle_animals': cats_cradle_animals})

def minn_kota(request):
    minn_kota_animals = Animal.objects.filter(shelter='Minn-Kota PAAWS')
    return render(request, 'animal_adoption_app/minn_kota.html', {'minn_kota_animals': minn_kota_animals})

def all_animals(request):
    all_animals = Animal.objects.all()
    return render(request, 'animal_adoption_app/all_animals.html', {'all_animals': all_animals})

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

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('index')
        else:
           
            return redirect('login')

    else:
        return render(request, 'animal_adoption_app/login.html', {})

def logout_user(request):
    logout(request)
    
    return redirect('index')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return redirect('index')
        else:
            
            return redirect('register')

    else:
        return render(request, 'animal_adoption_app/register.html', {'form' : form})


def filter_adopt(request):
    # Get all adopted animals
    animals = Animal.objects.filter(fosterable=False)

    # Get selected animal type from the form
    selected_animal_type = request.GET.get('animal_type')

    # Filter animals based on their type using hasattr
    filtered_animals = []
    for animal in animals:
        if hasattr(animal, 'dog'):
            animal_type = 'dog'
        elif hasattr(animal, 'cat'):
            animal_type = 'cat'
        elif hasattr(animal, 'lizard'):
            animal_type = 'lizard'
        elif hasattr(animal, 'bird'):
            animal_type = 'bird'
        elif hasattr(animal, 'fish'):
            animal_type = 'fish'
        else:
            animal_type = 'unknown'

        # If a specific animal type is selected, filter by that type
        if selected_animal_type and animal_type != selected_animal_type:
            continue

        filtered_animals.append((animal, animal_type))

    # Pass the filtered animals and selected animal type to the template
    context = {
        'adoption_list': filtered_animals,
        'selected_animal_type': selected_animal_type  # Pass the selected animal type to the template
    }
    return render(request, 'animal_adoption_app/adopt.html', context)


def filter_foster(request):
    # Get all fostered animals
    animals = Animal.objects.filter(fosterable=True)

    # Get selected animal type from the form
    selected_animal_type = request.GET.get('animal_type')

    # Filter animals based on their type using hasattr
    filtered_animals = []
    for animal in animals:
        if hasattr(animal, 'dog'):
            animal_type = 'dog'
        elif hasattr(animal, 'cat'):
            animal_type = 'cat'
        elif hasattr(animal, 'lizard'):
            animal_type = 'lizard'
        elif hasattr(animal, 'bird'):
            animal_type = 'bird'
        elif hasattr(animal, 'fish'):
            animal_type = 'fish'
        else:
            animal_type = 'unknown'

        # If a specific animal type is selected, filter by that type
        if selected_animal_type and animal_type != selected_animal_type:
            continue

        filtered_animals.append((animal, animal_type))

    # Pass the filtered animals and selected animal type to the template
    context = {
        'foster_list': filtered_animals,
        'selected_animal_type': selected_animal_type  # Pass the selected animal type to the template
    }
    return render(request, 'animal_adoption_app/foster.html', context)


def filter_homeward(request):
    # Get all animals at Homeward Shelter
    animals = Animal.objects.filter(shelter='Homeward Animal Shelter')

    # Get selected animal type from the form
    selected_animal_type = request.GET.get('animal_type')

    # Filter animals based on their type using hasattr
    filtered_animals = []
    for animal in animals:
        if hasattr(animal, 'dog'):
            animal_type = 'dog'
        elif hasattr(animal, 'cat'):
            animal_type = 'cat'
        elif hasattr(animal, 'lizard'):
            animal_type = 'lizard'
        elif hasattr(animal, 'bird'):
            animal_type = 'bird'
        elif hasattr(animal, 'fish'):
            animal_type = 'fish'
        else:
            animal_type = 'unknown'

        # If a specific animal type is selected, filter by that type
        if selected_animal_type and animal_type != selected_animal_type:
            continue

        filtered_animals.append((animal, animal_type))

    # Pass the filtered animals and selected animal type to the template
    context = {
        'homeward_animals': filtered_animals,
        'selected_animal_type': selected_animal_type  # Pass the selected animal type to the template
    }
    return render(request, 'animal_adoption_app/homeward.html', context)

def filter_cats_cradle(request):
    animals = Animal.objects.filter(shelter='Cats Cradle Shelter Inc')
    selected_animal_type = request.GET.get('animal_type')
    filtered_animals = []
    for animal in animals:
        if hasattr(animal, 'dog'):
            animal_type = 'dog'
        elif hasattr(animal, 'cat'):
            animal_type = 'cat'
        elif hasattr(animal, 'lizard'):
            animal_type = 'lizard'
        elif hasattr(animal, 'bird'):
            animal_type = 'bird'
        elif hasattr(animal, 'fish'):
            animal_type = 'fish'
        else:
            animal_type = 'unknown'
        if selected_animal_type and animal_type != selected_animal_type:
            continue
        filtered_animals.append((animal, animal_type))
    context = {
        'cats_cradle_animals': filtered_animals,
        'selected_animal_type': selected_animal_type
    }
    return render(request, 'animal_adoption_app/cats_cradle.html', context)


def filter_minn_kota(request):
    animals = Animal.objects.filter(shelter='Minn-Kota PAAWS')
    selected_animal_type = request.GET.get('animal_type')
    filtered_animals = []
    for animal in animals:
        if hasattr(animal, 'dog'):
            animal_type = 'dog'
        elif hasattr(animal, 'cat'):
            animal_type = 'cat'
        elif hasattr(animal, 'lizard'):
            animal_type = 'lizard'
        elif hasattr(animal, 'bird'):
            animal_type = 'bird'
        elif hasattr(animal, 'fish'):
            animal_type = 'fish'
        else:
            animal_type = 'unknown'
        if selected_animal_type and animal_type != selected_animal_type:
            continue
        filtered_animals.append((animal, animal_type))
    context = {
        'minn_kota_animals': filtered_animals,
        'selected_animal_type': selected_animal_type
    }
    return render(request, 'animal_adoption_app/minn_kota.html', context)

