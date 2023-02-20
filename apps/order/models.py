from django.db import models
from apps.authentication.models import User
from apps.store.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

PAYMENT_TYPES = (
    ("CashOnDelivery", "Cash On Delivery"),
    ("DebitCards", "Debit Cards"),
    ("MobilePayment", "Mobile Payment"),
    ("TraditionalTransfer", "Traditional Transfer"),
)


class Discount(models.Model):
    name = models.CharField(max_length=255, unique=True)
    percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                              validators=PERCENTAGE_VALIDATOR)


class Payment(models.Model):
    payment_type = models.CharField(max_length=255 ,choices=PAYMENT_TYPES, blank=False)
    deadline = models.DateField(blank=False)
    is_paid = models.BooleanField(blank=False)


class Order(models.Model):
    date_created = models.DateField(auto_now=True)
    country = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=False)
    postal_code = models.CharField(max_length=255, blank=False)
    client = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='order_client', blank=False)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, related_name='order_payment', blank=False)
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, related_name='order_discount', blank=True)


class Cart(models.Model):
    client = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart_order', blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product', blank=False)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
