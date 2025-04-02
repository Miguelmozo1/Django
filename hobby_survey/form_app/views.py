from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def submit(request):
    if len(request.POST['name']) > 1:
        request.session['name'] = request.POST['name']
    else:
        return redirect("/")
    if len(request.POST['favorite_hobby']) > 1:
        request.session['favorite_hobby'] = request.POST['favorite_hobby']
    else:
        return redirect("/")
    request.session['indoor'] = request.POST['indoor']
    request.session['req'] = request.POST['req']
    request.session['type'] = request.POST['type']
    if len(request.POST['comment']) > 1 or len(request.POST['comment']) == 0:
        request.session['comment'] = request.POST['comment']
    else:
        return redirect("/")
    return redirect("/show")

def show(request):
    data = {
        'name': request.session['name'],
        'hobby': request.session['favorite_hobby'],
        'indoor': request.session['indoor'],
        'required': request.session['req'],
        'type': request.session['type'],
        'comment': request.session['comment']
    }
    return render(request, 'show.html', data)