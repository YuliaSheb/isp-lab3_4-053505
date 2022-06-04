from django.shortcuts import render
from .models import Cake
from .models import Feedback
from .forms import CakeForm
from .forms import FeedbackForm


def index(request):
    cakes = Cake.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'cakes': cakes})


def about(request):
    return render(request, 'main/about.html')


def admin_main(request):
    return render(request, 'main/admin_main.html')


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
    feedbacks = Feedback.objects.all()
    return render(request, 'main/review.html', {'title': 'Отзывы', 'feedbacks': feedbacks})


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
