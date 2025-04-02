from django.shortcuts import render, HttpResponse, redirect
from .models import Gym, Folks

# Create your views here.


def root(request):
    context = {
        'gyms': Gym.objects.all(),
        'folks': Folks.objects.all(),
    }
    return render(request, "root.html", context)

def create_gym(request):
    Gym.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['city'])
    return redirect('/')


def create_folk(request):
    Folks.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], gym=Gym.objects.get(id=request.POST['gym']))
    return redirect('/')

def delete(request, id):
    gym = Gym.objects.get(id = id)
    gym.delete()
    return redirect('/')