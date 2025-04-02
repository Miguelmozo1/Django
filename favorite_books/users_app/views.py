from django.shortcuts import render, redirect
import bcrypt
from .models import User
from django.contrib import messages

# Create your views here.


def register(request):
    if 'email_error' in request.session:
        del request.session['email_error']
    results = User.objects.filter(email = request.POST['email'])
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if len(results) > 0:
        request.session['email_error'] = "Email already taken, please try another one"
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        request.session['userid'] = user.id
    return redirect("/success")


def login(request):
    if len(request.POST['email']) == 0 or len(request.POST['password']) == 0:
        request.session['email_error'] = "Please, no empty submissions"
        exit
        return redirect('/')
    if 'email_error' in request.session:
        del request.session['email_error']
    user = User.objects.filter(email = request.POST['email'])
    if not user:
        request.session['email_error'] = "Invalid Login"
        return redirect('/')
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
    return redirect('/')