from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('admin_main', views.admin_main, name='admin_main'),
    path('review', views.review, name='review'),
    path('create_review', views.create_review, name='create_review'),
    path('gallery', views.gallery, name='gallery'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path("registration", views.registration, name="registration"),
    path("login", views.loginP, name="login"),
    path("logout", views.logoutUser, name="logout"),
    ]


if settings.DEBUG:
    urlpatterns+=staticfiles_urlpatterns()+static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

