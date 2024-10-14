from django.shortcuts import render
from store.models import Product, ReviewRating
from datetime import datetime

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')
    year = datetime.now().year
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    context = {
        'products': products,
        'reviews': reviews,
        'year': year,
    }
    return render(request,'home.html',context)