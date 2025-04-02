from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'courses': Course.objects.all()

    }
    return render(request, "index.html", context)

def delete(request,id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'delete.html', context)


def comments(request,id):
    context = {
        'course': Course.objects.get(id=id),
        "comments": Comment.objects.filter(course=Course.objects.get(id=id))
    }
    return render(request, "comments.html", context)









def create_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        course = Course.objects.create(name=request.POST['name'])
        description = Description.objects.create(description=request.POST["description"], course= course)
        messages.success(request, "Show successfully Created")
    return redirect("/")





def delete_course(request, id):
    ans = request.POST['delete']
    match ans:
        case "no":
            return redirect("/")
        case "yes":
            c = Course.objects.get(id=id)
            c.delete()
            c.save
            return redirect("/")
    return redirect("/")




def create_comment(request, id):
    comment = Comment.objects.create(comment=request.POST['comment'], course= Course.objects.get(id=id))
    return redirect(f'/comments/{id}')