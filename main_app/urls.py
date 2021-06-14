from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('animals/',                      views.AnimalList.as_view(),   name='animals_index'),
  path('animals/<int:pk>/',             views.animal_detail,          name='animals_detail'),
  path('animals/create/', views.AnimalCreate.as_view(), name='animals_create'),
  path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update'),
  path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animals_delete'),
  path('animals/<int:pk>/add_feeding/', views.add_feeding,         name='add_feeding'),
]