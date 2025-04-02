from django.shortcuts import render, redirect
from users_app.models import User
from books_app.models import Book

# Create your views here.

def index(request):
    # say a user decides to finally leave the site and decides to come back and try and bypass login by changing url, this prevents it
    if 'userid' in request.session:
        del request.session['userid']
    return render(request, "index.html")

def home(request):
    if 'userid' not in request.session:
        return redirect('/')
    user = User.objects.get(id = request.session['userid'])
    likes = user.favorites.all
    context = {
        'user': user,
        'books': Book.objects.all(),
        'likes': likes,
    }
    return render(request, 'home.html', context)



def logout(request):
    del request.session['userid']
    return redirect("/")