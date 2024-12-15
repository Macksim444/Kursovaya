from lib2to3.fixes.fix_input import context
from multiprocessing.managers import BaseManager

from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


from goods.models import Categories

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def index(request):

    categories: BaseManager[Categories] = Categories.objects.all()
    context: dict[str, str] = {
        'title': 'Home - Главная',
        'content': "Зоопарк Koala's smile",
        'categories': categories
    }
    return render(request, 'realtyestateapp/index.html',  context)


def about(request):
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content': "О нас",
        "text_on_page": "Зоопарк прекрасный, животные топи-топ"
    }
    return render(request, 'realtyestateapp/about.html', context)

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    contex = {
        'form': form,
        'error': error
    }
    return render(request, 'realtyestateapp/create.html', contex)

def catalog(request):
    return render(request, 'realtyestateapp/catalog.html')

def product(request):
    return render(request, 'realtyestateapp/product.html')


