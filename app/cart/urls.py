from django.urls import path, re_path
from . import views

app_name = 'cart'

urlpatterns = [
    path(r'', views.cart_detail, name='cart-detail'),
    path(r'increase/<int:product_id>', views.cart_increase, name='increase-item'),
    path(r'decrease/<int:product_id>', views.cart_decrease, name='decrease-item'),
]
