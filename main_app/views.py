from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import FeedingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# View functions

# Define the home view
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

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
    return Animal.objects.filter(user=self.request.user)

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

  def form_valid(self, form):
    # Assign the logged in user
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['name', 'description', 'age']
  success_url = '/animals/'

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'