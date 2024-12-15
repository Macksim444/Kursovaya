from email.policy import default

from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, null=False, verbose_name='URL')

    class Meta:
        db_table: str = 'category'
        verbose_name: str = 'Категорию'
        verbose_name_plural: str = 'Категории'
    def __str__(self):
        return self.name

class TicketCategories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, null=False, verbose_name='URL')

    class Meta:
        db_table = 'ticket'
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to = 'goods_images', blank=True, null=True, verbose_name = 'Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default = 0.00, max_digits=7, decimal_places=2, verbose_name = 'Скидка в %')
    quality = models.PositiveIntegerField(default = 0, verbose_name = 'Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table: str = 'product'
        verbose_name: str = 'Билет'
        verbose_name_plural: str = 'Билеты'

    def __str__(self):
        return f'{self.name} Количество - {self.quality}'
    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)

        return self.price

class Animals(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    quality = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'animal'
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self):
        return f'{self.name} Количество - {self.quality}'

    def display_id(self):
        return f"{self.id:05}"
    # Create your models here.