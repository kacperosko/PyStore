from decimal import Decimal
from django.conf import settings
from .models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['total_price'] = float(item['price']) * int(item['quantity'])
            yield item

    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity == "true":
            self.cart[product_id]['quantity'] = int(quantity)
            print("TEST_true", self.cart[product_id]['quantity'])
        else:
            self.cart[product_id]['quantity'] += int(quantity)
            print("TEST_false", self.cart[product_id]['quantity'])
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return round(sum(float(item['price']) * int(item['quantity']) for item in self.cart.values()), 2)

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]

    # def add_discount(self, name, size):
    #     self.cart['discount'] = {'name': name, 'size': size} #There should be one discount at the same time
    #
    # def get_discount(self):
    #     return self.cart['discount']

    def get_total_price_discount(self):
        discount = self.session.get('discount', None)
        print(discount)
        if discount is None or 'discount_percentage' not in discount:
            return
        result = round(self.get_total_price() * (discount['discount_percentage'] / 100), 2)
        return result
