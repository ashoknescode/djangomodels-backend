from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person

# Create your views here.
def homepage(request):
	persons = Person.objects.all()
	return render(request, 'homepage.html', {'persons': persons})