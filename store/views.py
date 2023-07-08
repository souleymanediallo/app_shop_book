from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product, Cart, Order


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/index.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse('product_detail', kwargs={'slug': slug}))