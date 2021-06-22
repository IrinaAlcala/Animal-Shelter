from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import FeedingForm

# View functions

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def animals_index(request):
  animals = Animal.objects.all()
  return render(request, 'animals/index.html', { 'animals': animals })

class AnimalList(ListView):
  model = Animal

def get_queryset(self):
    return Animal.objects.all()

def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  feeding_form = FeedingForm()
  return render(request, 'animals/detail.html', {
    'animal': animal,
    'feeding_form': feeding_form,
  })

def add_feeding(request, animal_id):
  form = FeedingForm(request.POST, request.FILES)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.animal_id = animal_id
    new_feeding.save()
  return redirect('detail', animal_id=animal_id)

class AnimalCreate(CreateView):
  model = Animal
  fields = '__all__' # means ['name', 'breed', 'description', 'age']
  success_url = '/animals/'

class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['name', 'description', 'age']
  success_url = '/animals/'

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'