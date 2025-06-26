from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm
from django.utils import timezone
from .models import Feedback,Product
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash password
            user.date_joined = timezone.now()
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'html/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You are successfully logged in to your account.")
            return redirect('dashboard')  # redirect after success
    else:
        form = LoginForm()
    return render(request, 'html/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'html/dashboard.html')

def feedback_form(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        remark = request.POST.get('remark')
        Feedback.objects.create(rating=rating, remark=remark)
        return JsonResponse({'message': 'Feedback submitted successfully!'})
   # return JsonResponse({"message":"Not Submitted"})
    return render(request,'html/feedback.html')

def Cart_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('pro_name')
        product_price = request.POST.get('pro_price')
        product_image = request.POST.get('pro_image')  # This is just the path, not actual upload
        product_quantity = request.POST.get('pro_quantity')

        Product.objects.create(
            product_name=product_name,
            product_price=product_price,
            product_image=product_image,  # Should be a valid relative path like 'products/moto.png'
            product_quantity=product_quantity
        )

        return JsonResponse({'message': 'Item added successfully in cart'})
    else:
        return render(request, 'html/cart.html')
'''
def view_cart(request):
    cart_items = Product.objects.all()
    return render(request, 'html/cart.html', {'cart_items': cart_items})
'''
def view_cart(request):
    cart_items = Product.objects.all()
    total_price = sum(item.product_price * item.product_quantity for item in cart_items)
    return render(request, 'html/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def delete_cart_item(request, item_id):
    item = get_object_or_404(Product, id=item_id)
    item.delete()
    return redirect('view_cart')

def chatbox(request):
    return render(request,'html/chat.html')