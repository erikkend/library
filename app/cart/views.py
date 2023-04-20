from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.http import require_POST
from books.models import Book
from cart.cart import Cart


@require_POST
def cart_increase(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.increase_product(product=product, quantity=+1)

    do_redirect = True
    if "/books/" in str(request.META['HTTP_REFERER']):
        do_redirect = False

    if do_redirect:
        return redirect('cart:cart-detail')
    else:
        return redirect(reverse("book-detail", kwargs={"pk": product_id}))


@require_POST
def cart_decrease(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.decrease_product(product=product, quantity=1)
    return redirect('cart:cart-detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart-detail.html', {"cart": cart})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.remove_product(product)
    return redirect('cart:cart-detail')
