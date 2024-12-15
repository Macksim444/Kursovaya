from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание') #Большое количество текста

    def __str__(self):
        return self.title #Миграция для таблиц БД

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

"""class Animals(models.Model):
    animal = models.CharField('Вид', max_length=50)
    name = models.CharField('имя', max_length=20)
    task_animal = models.TextField('О виде')
    def __str__(self):
        return self.animal

    class Meta:
        verbose_name = 'Вид'
        verbose_name_animal = 'Имя'
        verbose_name_plural = 'О виде'"""

