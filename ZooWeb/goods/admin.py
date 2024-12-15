from django.contrib import admin

from goods.models import Categories, Products, Animals, TicketCategories


#admin.site.register(Categories)
#admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(TicketCategories)
class TicketCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
# Register your models here.
