from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,'index.html')

def welcome(request):
    user=User.objects.get(id=request.session['user_id'])
    context = {
        'user':user
        
    }
    messages.error(request, "successfuly registered")
    return render(request,'welcome.html', context)

def submit(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['firstname'],last_name=request.POST['lastname'],email=request.POST['email'],password=hash1)
        user = User.objects.last()
        request.session['user_id'] = user.id
        return redirect('/welcome')


