# создадим внутри директории cart файл cart.py и заполним его следующим:

from django.conf import settings
from books.models import Book


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем корзину пользователя в сессию
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save_to_session(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def increase_product(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                                    'quantity': 0,
                                    'price': str(product.price)
                                }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save_to_session()

    def decrease_product(self, product, quantity=1):
        product_id = str(product.id)
        if self.cart[product_id]['quantity'] > 1:
            self.cart[product_id]['quantity'] -= quantity
        else:
            self.remove_product(product)
        self.save_to_session()

    def remove_product(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save_to_session()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Book.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def get_product_count(self):
        return len(self.cart.items())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
