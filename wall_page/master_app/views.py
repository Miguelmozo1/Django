from django.shortcuts import render, redirect
import bcrypt
from .models import User
from messages_app.models import Message
from django.contrib import messages

# Create your views here.

def index(request):
    if 'userid' in request.session:
        del request.session['userid']
    return render(request, "index.html")

def home(request):
    if 'userid' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'messages': Message.objects.all()
    }
    return render(request, "home.html", context)












def register(request):
    if 'email_error' in request.session:
        del request.session['email_error']
    results = User.objects.filter(email=request.POST['email'])
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    if len(results) > 0:
        request.session['email_error'] = "Email taken, use different one"
        return redirect("/")
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        request.session['user_id'] = user.id
    return redirect("/home")


def login(request):
    email = request.POST['email']
    password = request.POST['password']
    if len(email) == 0 or len(password) == 0:
        request.session['email_error'] = "Please fill out email or password"
        exit
        return redirect("/")
    if len(email) < 8 or len(password) < 8:
        request.session['email_error'] = "Email and Password must be at least 8 characters"
        exit
        return redirect("/")
    if 'email_error' in request.session:
        del request.session['email_error']
    user = User.objects.filter(email = request.POST['email'])
    if not user:
        return redirect("/")
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/home')
    request.session['email_error'] = "Invalid Login"
    print(request.POST)
    return redirect("/")


def destroy(request):
    del request.session['userid']
    return redirect('/')