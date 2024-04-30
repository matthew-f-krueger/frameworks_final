from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello World!")
    my_dict={'insert_me': 'Cats are cool and stuff'}
    return render(request, 'animal_adoption_app/index.html', context=my_dict)