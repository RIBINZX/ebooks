from django.shortcuts import render
from .models import Product

# Create your views here.
def shop_details(request,id):
    product=Product.objects.get(id=id)
    context = {"product": product}
    return render(request, "web/shop-detail.html", context)

def shop(request):
    language_filter = request.GET.get('language', '')
    products = Product.objects.all()
    if language_filter:
        products = products.filter(language=language_filter)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)



    context = {"product": products, "request": request} # Pass the request object to the template context
    return render(request, "web/shop.html", context)



def signup(request,):

    return render(request, "web/signup.html")

def login(request,):

    return render(request, "web/login.html")