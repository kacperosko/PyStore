# Generated by Django 4.1.5 on 2023-01-13 18:33

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percentage', models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('CashOnDelivery', 'on delivery'), ('DebitCards', 'Debit cards'), ('MobilePayment', 'Mobile payment'), ('TraditionalTransfer', 'Traditional transfer')], max_length=255)),
                ('deadline', models.DateField()),
                ('is_paid', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now=True)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_client', to=settings.AUTH_USER_MODEL)),
                ('discount', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_discount', to='order.discount')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_payment', to='order.payment')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_order', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='store.product')),
            ],
        ),
    ]
