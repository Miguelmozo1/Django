from django.shortcuts import render, redirect
from .models import Message
from master_app.models import User

# Create your views here.

def create_message(request):
    userid= request.session['userid']
    if len(request.POST['message']) < 5:
        request.session['mess_error'] = "Message must be at least 5 characters long"
        exit
        return redirect("/home")
    else:
        del request.session['mess_error']
        Message.objects.create(message=request.POST['message'], user = User.objects.get(id=userid))
    return redirect("/home")


def delete_message(request):
    message = Message.objects.get(id=request.session['userid'])
    message.delete()
    message.save
    return redirect("/home")