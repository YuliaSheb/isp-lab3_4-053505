from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('admin_main', views.admin_main, name='admin_main'),
    path('review', views.review, name='review'),
    path('create_review', views.create_review, name='create_review'),
]
