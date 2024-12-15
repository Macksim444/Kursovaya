from django.urls import path
from . import views

app_name = 'realtyestateapp'
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('admin', views.signup, name='admin'),
    path('signup', views.signup, name='signup'),
]
