from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product

from django.http import HttpResponse
from .models import Comment

from django.http import JsonResponse
# Create your views here.



from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

def shop_details(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_content = request.POST.get('comment')
            if comment_content and comment_content.strip():
                comment = Comment(content=comment_content, product=product, user=request.user)
                comment.save()
                return JsonResponse({'success': True, 'username': request.user.username, 'comment': comment_content})
            else:
                return JsonResponse({'success': False, 'message': 'Comment cannot be empty.'})
        else:
            return JsonResponse({'success': False, 'message': 'Authentication required'})

    comments = Comment.objects.filter(product=product)
    context = {"product": product, 'comments': comments}
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




def signup(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            print('Passwords do not match')
            return redirect('web:signup')
        else:
            if User.objects.filter(username=username).exists():
                print('User already exists')
                return redirect('web:signup')
            else:
                user = User.objects.create_user(username=username, password=password1)
                return redirect('web:login')

    return render(request, 'web/signup.html')





def login_1(request,):

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('web:shop')
        else:  
            print('hi')
            return redirect('web:signup')
    return render(request,"web/login.html")



def logout_view(request):
    logout(request)
    return redirect('web:shop')