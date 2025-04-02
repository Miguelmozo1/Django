from django.shortcuts import render, redirect
from .models import Movie
from users_app.models import User

# Create your views here.


def add(request):
    return render(request, 'add.html')

def movie(request, id):
    movie = Movie.objects.get(id=id)
    context = {
        'movie': movie
    }
    return render(request, 'movie.html', context)


def create(request):
    user = User.objects.get(id = request.session['userid'])
    movie = Movie.objects.create(
        title = request.POST['title'],
        director = request.POST['director'],
        user = user
    )
    return redirect(f'/movies/movie/{movie.id}')