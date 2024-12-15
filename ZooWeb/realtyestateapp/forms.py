from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }

"""class Animals(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "name-animal","aboutAnimal"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вид животного'
            }),
            "name-animal": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя животного'
            }),
            "aboutAnimal": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание животного'
            })
        }"""
