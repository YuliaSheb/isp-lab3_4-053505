from django.shortcuts import render
from .models import Cake
from .models import Feedback
from .forms import CakeForm
from .forms import FeedbackForm
from django.http import HttpResponseNotFound
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib import messages
import logging
import asyncio
from asgiref.sync import sync_to_async
from django.contrib.auth import authenticate, login, logout


def index(request):
    logging.info('Welcome')
    cakes = Cake.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'cakes': cakes})


def main(request):
    cakes = Cake.objects.all()
    return render(request, 'main/main.html', {'title': 'Главная страница', 'cakes': cakes})


def gallery(request):
    return render(request, 'main/gallery.html')


def edit(request, id):
    try:
        cake = Cake.objects.get(id=id)

        if request.method == "POST":
            cake.name = request.POST.get("name")
            cake.anons = request.POST.get("anons")
            cake.price = request.POST.get("price")
            cake.save()
            return render(request, 'main/admin_main.html')
        else:
            return render(request, 'main/edit.html', {"cake": cake})
    except Cake.DoesNotExist:
        return HttpResponseNotFound("<h2>Cake not found</h2>")


# удаление данных из бд
def delete(request, id):
        cake = asyncio.run(async_delete())
        if request.method == 'POST':
            cake.delete()
            return redirect('admin_main')

        context = {
            'form': cake
        }
        return render(request, 'main/admin_main.html', context)

@sync_to_async
def async_delete(id):
    cake = Cake.objects.get(id=id)
    return cake

def about(request):
    return render(request, 'main/about.html')


def admin_main(request):
    cakes = Cake.objects.all()
    return render(request, 'main/admin_main.html',{'title': 'Главная страница', 'cakes': cakes})


def create(request):
    if request.method == 'POST':
        form = CakeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Данные введены не верно'

    form = CakeForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

def review(request):
    feedbacks = asyncio.run(review_obj())
    return render(request, 'main/review.html', {'title': 'Отзывы', 'feedbacks': feedbacks})

@sync_to_async
def review_obj():
    feedbacks = Feedback.objects.all()
    return feedbacks

def create_review(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Данные введены не верно'

    form = FeedbackForm()
    context = {
        'form': form
    }
    return render(request, 'main/create_review.html', context)


def registration(request):
    form = CreateUserForm()


    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for "+ user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'main/registration.html',context)


def loginP(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Username or password is incorrect")

    context = {}
    return render(request, 'main/login.html',context)

def logoutUser(request):
    return redirect('login')
