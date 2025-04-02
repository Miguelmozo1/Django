from django.shortcuts import render, redirect
from register_app.models import User
import bcrypt
from django.contrib import messages


# Create your views here.

def login(request):
    if len(request.POST['email']) == 0 or len(request.POST['password']) == 0:
        request.session['email_error'] = "Please fill out email or password"
        exit
        return redirect("/")
    if 'email_error' in request.session:
        del request.session['email_error']
    user = User.objects.filter(email = request.POST['email'])
    # try commenting out line 12 and 13
    if not user:
        return redirect("/")
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
    request.session['email_error'] = "Invalid Login"
    return redirect("/")