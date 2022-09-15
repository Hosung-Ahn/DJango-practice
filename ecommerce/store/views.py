from django.shortcuts import get_object_or_404, render
from category.models import Category
from . import models


# Create your views here.

def store(request, category_slug=None) :
    categories = None
    product = None
    
    if category_slug != None :
        categories = get_object_or_404(Category, slug=category_slug)
        products = models.Product.objects.all().filter(category=categories, is_available=True)
        product_count = products.count()
    else :
        products = models.Product.objects.all().filter(is_available = True)
        product_count = products.count()
    
    context = {'products' : products,
               'product_count' : product_count,
               'category_slug' : category_slug, }
    return render(request, 'store/store.html', context)