from django.shortcuts import render, redirect
from .models import Comment
from django.contrib import messages
from master_app.models import User
from messages_app.models import Message

# Create your views here.

def create_comment(request):
    errors = Comment.objects.basic_validator(request.POST)
    userid= request.session['userid']
    messageid = request.POST['message_id']
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/home')
    else:
        Comment.objects.create(
            comment = request.POST['comment'],
            user = User.objects.get(id=userid),
            message = Message.objects.get(id=messageid)
        )
    return redirect("/home")