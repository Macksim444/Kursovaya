from django.db.models.manager import BaseManager
from django.shortcuts import render
from django.core.paginator import Paginator
from goods.models import Products, Animals
from goods.utils import q_search

def animalcatalog(request, ticket_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)


    if ticket_slug == "all":
        goods = Animals.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Animals.objects.filter(ticket__slug=ticket_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context: dict[str, str] = {
        'title': 'Home - Каталог',
        'goods': current_page,
        "slug_url": ticket_slug
    }
    return render(request, 'goods/animalcatalog.html', context)

def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)


    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context: dict[str, str] = {
        'title': 'Home - Каталог',
        'goods': current_page,
        "slug_url": category_slug
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context: dict[str, Products] = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context)
