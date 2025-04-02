from django.shortcuts import render, redirect
from .models import Book
from users_app.models import User

# Create your views here.

def book(request, id):
    book = Book.objects.get(id=id)
    user = User.objects.filter(id = request.session['userid'])
    context = {
        'book': book,
        'user': user
    }
    if request.session['userid'] == book.user.id:
        return render(request, 'edit.html', context)
    return render(request, "book.html", context)


def create_book(request):
    user = User.objects.get(id = request.session['userid'])
    book = Book.objects.create(title=request.POST['title'], description=request.POST['description'], user=user)
    favorite = Book.objects.get(id=book.id)
    favorite.liked_by.add(user)
    favorite.save()
    return redirect('/success')


def update(request):
    b = Book.objects.get(id=request.POST['book_id'])
    if request.POST['btn'] == 'update':
        book = b
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.save()
    else:
        book = b
        book.delete()
        book.save()
    return redirect('/success')


def add(request, id):
    user = User.objects.get(id = request.session['userid'])
    book = Book.objects.get(id=id)
    book.liked_by.add(user)
    book.save()
    return redirect(f'/books/{id}')


def remove(request, id):
    user = User.objects.get(id = request.session['userid'])
    book = Book.objects.get(id=id)
    book.liked_by.remove(user)
    book.save()
    return redirect(f'/books/{id}')