from django.shortcuts import render, redirect
import bcrypt
from .models import User
from django.contrib import messages

# Create your views here.










def register(request):
    if 'email_error' in request.session:
        del request.session['email_error']
    results = User.objects.filter(email=request.POST['email'])
    print(len(results))
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if len(results) > 0:
        request.session['email_error'] = "Email taken, please use another Email"
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
    return redirect("/success")