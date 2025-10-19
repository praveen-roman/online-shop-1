from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post

from django.contrib.auth.decorators import login_required
from .models import Post, CartItem

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Post, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})


@login_required
def increase_quantity(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def decrease_quantity(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # remove item if quantity goes below 1
    return redirect('cart')

@login_required
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    # You can later add payment processing logic here
    cart_items = request.user.cart_items.all()  # if you have related_name='cart_items'
    total = sum(item.product.offer_price * item.quantity for item in cart_items)
    return render(request, 'shop/checkout.html', {'cart_items': cart_items, 'total': total})

def home(request):
    # Get 4 latest active posts for Men
    men_posts = Post.objects.filter(is_active=True, category='Men').order_by('-created_at')[:4]

    # Get 4 latest active posts for Women
    women_posts = Post.objects.filter(is_active=True, category='Women').order_by('-created_at')[:4]

    return render(request, 'shop/index.html', {
        'men_posts': men_posts,
        'women_posts': women_posts,
    })
def women(request):
    women_posts=Post.objects.filter(is_active=True,category='Women').order_by('created_at')
    return render(request,'shop/women.html',{'women_posts':women_posts})



def women_product(request, pk):
    product = get_object_or_404(Post, pk=pk)
    return render(request, 'shop/womenproduct.html', {'product': product})


def men(request):
    men_posts=Post.objects.filter(is_active=True,category='Men').order_by('created_at')
    return render(request,'shop/men.html',{'men_posts':men_posts})



def men_product(request, pk):
    product = get_object_or_404(Post, pk=pk)
    return render(request, 'shop/menproduct.html', {'product': product})