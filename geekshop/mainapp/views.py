import json

from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.conf import settings

def index(request):

    products_list = Product.objects.all()[:4]

    context = {
        'title': 'мой магазин',
        'products': products_list
    }

    return render(request, 'mainapp/index.html', context)


def contact(request):
    with open(f'{settings.BASE_DIR}/contacts.json') as contacts_file:
        context = {
            'contacts': json.load(contacts_file)
        }
    return render(request, 'mainapp/contact.html', context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, 'mainapp/products.html', context)