from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CakeForm(ModelForm):
    class Meta:
        model = Cake
        fields = ["name","anons","price"]
        widgets = {
            "name":TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Введите название'
        }),
        "anons": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Описание'
        }),
        "price": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Цена'
        }),
    }


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["name_u","review_u"]
        widgets = {
            "name_u":TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Введите имя'
        }),
        "review_u": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Отзыв'
        }),
    }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
