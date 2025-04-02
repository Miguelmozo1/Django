from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0;
    data = {
        "data": request.session['counter']
    }
    return render(request, "index.html", data)


def two(request):
    if 'counter' in request.session:
        request.session['counter'] += 1;
    return redirect('/')

def custom(request):
    custom = request.POST['num']
    if 'counter' in request.session:
        request.session['counter'] += int(custom) - 1;
    return redirect("/")

def reset(request):
    del request.session['counter']
    return redirect("/")