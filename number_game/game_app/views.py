from django.shortcuts import render, redirect
import random


# Create your views here.


def root(request):
    request.session['goal'] = random.randint(1,100)
    request.session['attempt'] = '';
    request.session['class'] = '';
    request.session['attempts'] = 0;
    return redirect("/index")

def index(request):
    context = {
        'num': request.session['goal'],
        'input': request.session['attempt'],
        'class': request.session['class'],
        'attempts': request.session['attempts']
    }
    return render(request, "index.html" , context)

def attempt(request):
    if request.session['attempts'] == 5 - 1:
        return redirect("/lose")
    request.session['attempts'] += 1
    if len(request.POST['attempt']) < 1:
        return redirect("/index")
    attempt = int(request.POST['attempt']);
    request.session['attempt'] = request.POST['attempt']
    goal = request.session['goal']
    if int(attempt) == goal:
        request.session['class'] = "green"
    if int(attempt) < goal:
        request.session['class'] = "red"
    if int(attempt) > goal:
        request.session['class'] = "yellow"
    return redirect("/index")

def lost(request):
    return render(request, 'lost.html')



def reset(request):
    del request.session['goal']
    del request.session['attempt']
    del request.session['attempts']
    return redirect("/")