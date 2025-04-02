from django.shortcuts import render, redirect
from register_app.models import User

# Create your views here.

def index(request):
    if 'userid' in request.session:
        del request.session['userid']
    return render(request, "index.html")

def success(request):
    if 'userid' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['userid'])
    }
    return render(request, "success.html", context)

def destroy(request):
    del request.session['userid']
    return redirect("/")