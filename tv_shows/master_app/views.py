from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages


# Create your views here.

def root(request):
    return redirect('/shows')

def shows(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, "root.html", context)

def create_show(request):
    return render(request, "create_show.html")

def show(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    print(show.release_date)
    return render(request, "show.html", context)

def edit_show(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, "edit.html", context)



# action functions
def add_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/create/show')
    else:
        x = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        messages.success(request, "Show successfully Created")
    return redirect(f'/shows/show/{x.id}')

def delete_show(request, id):
    x = Show.objects.get(id=id)
    x.delete()
    x.save
    return redirect("/shows")

def update_show(request):
    id = request.POST["show_id"]
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/edit/'+id)
    else:
        id = request.POST["show_id"]
        show = Show.objects.get(id = id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        messages.success(request, "Show successfully updated")
        return redirect(f'/shows/show/{id}')
