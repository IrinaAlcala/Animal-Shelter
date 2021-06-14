from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import FeedingForm

# View functions

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class AnimalList(ListView):
  model = Animal

  def get_queryset(self):
    return Animal.objects.all()

def animal_detail(request, pk):
  animal = Animal.objects.get(id=pk)
  feeding_form = FeedingForm()
  return render(request, 'main_app/animal_detail.html', {
    'animal': animal,
    'feeding_form': feeding_form
  })

def add_feeding(request, pk):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.animal_id = pk
    new_feeding.save()
  return redirect('animals_detail', pk=pk)

class AnimalCreate(CreateView):
  model = Animal
  fields = '__all__' # means ['name', 'breed', 'description', 'age']

class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['name', 'description', 'age']

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'