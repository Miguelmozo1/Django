from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

def root(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request, "root.html", context)

def authors(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render(request, "authors.html", context)

def book(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book' : book,
        'authors': book.authors.all(),
        'non': Author.objects.exclude(books=book)
    }
    return render(request, "book.html", context)

def author(request, id):
    author = Author.objects.get(id = id)
    context ={
        'author': author,
        'books': author.books.all(),
        'non': Book.objects.exclude(authors= author)
    }
    return render(request, "author.html", context)


def create_book(request):
    Book.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect("/")

def create_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect("/authors")


def join_author(request):
    book = Book.objects.get(id=request.POST['book'])
    author = Author.objects.get(id=request.POST['author_id'])
    author.books.add(book)
    author.save()
    return redirect(f'/author/{request.POST['author_id']}')

def join_book(request):
    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=request.POST['author'])
    book.authors.add(author)
    book.save()
    return redirect(f'/book/{request.POST['book_id']}')