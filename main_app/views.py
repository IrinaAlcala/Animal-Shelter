from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Animal

# View functions

class AnimalCreate(CreateView):
    model = Animal
    fields = ['name', 'type', 'description', 'age']
    success_url = '/animals/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def animals_index(request):
  animals = Animal.objects.all()
  return render(request, 'animals/index.html', { 'animals': animals })

def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  return render(request, 'animals/detail.html', { 'animal': animal })

  
  