from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')


def animals_index(request):
    return render(request, 'animals/index.html', { 'animals': animals })