from django.shortcuts import render, redirect, HttpResponse
import random

# Create your views here.


def root(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    context = {
        'gold': request.session['gold'],
        'activities': request.session['log']
    }
    return render(request, 'index.html', context)

def gold(request):
    source = request.POST['name']
    match source:
        case "river":
            x = random.randint(1,8)
            request.session['gold'] += x
            request.session['log'].append("You collected:" + " " + str(x) + " " + "gold(s)")
        case "steal":
            x = random.randint(1,5)
            request.session['gold'] += x
            request.session['log'].append("You collected:" + " " + str(x) + " " + "gold(s)")
        case "casino":
            x = random.randint(-50,50)
            request.session['gold'] += x
            if x >= 0:
                request.session['log'].append("You collected:" + " " + str(x) + " " + "gold(s)")
            if x < 0:
                request.session['log'].append("You lost:" + " " + str(x) + " " + "gold(s)")
        case "beg":
            x = random.randint(1,6)
            request.session['gold'] += x
            request.session['log'].append("You collected:" + " " + str(x) + " " + "gold(s)")
    print(request.session['log'])
    return redirect('/')

def reset(request):
    del request.session['gold'];
    del request.session['log'];
    return redirect("/")