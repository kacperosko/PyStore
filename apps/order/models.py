from django.db import models
from apps.authentication.models import User, Unregistered_User, Address
from apps.store.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
from apps._custom_models.custom_models import UpperCaseCharField

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

PAYMENT_TYPES = (
    ("CashOnDelivery", "Cash On Delivery"),
    ("DebitCards", "Debit Cards"),
    ("MobilePayment", "Mobile Payment"),
    ("TraditionalTransfer", "Traditional Transfer"),
)


class Discount(models.Model):
    name = UpperCaseCharField(max_length=255, unique=True)
    percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                     validators=PERCENTAGE_VALIDATOR)

    def __str__(self):
        return f"{self.name} -{self.percentage}"


class Payment_Type(models.Model):
    payment_name = models.CharField(max_length=255, blank=False)


class Payment(models.Model):
    payment_type = models.ForeignKey(Payment_Type, on_delete=models.DO_NOTHING, related_name='payment_type')
    deadline = models.DateField(blank=False)
    is_paid = models.BooleanField(blank=False)


class Order(models.Model):
    date_created = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='order_user', blank=True, null=True)
    unregistered_user = models.ForeignKey(Unregistered_User, on_delete=models.DO_NOTHING,
                                          related_name='order_unregistered_user', blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, related_name='order_payment', blank=True,
                                null=True)
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, related_name='order_discount', blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='order_address', blank=True, null=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return f"Order {self.id}, {self.date_created}"


class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item_order', blank=False)
    # selected_attributes = models.CharField(max_length=500, blank=True)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item_product', blank=False,
                                null=True)


class Cart_Item(models.Model):
    client = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart_order', blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product', blank=False)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
