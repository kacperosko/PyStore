from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.order.models import Order, Order_Item
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url='/login/')
def get_user_account_orders(request):
    content = {'n': range(10)}

    orders = Order.objects.filter(user=request.user)
    for o in orders:
        o.amount = sum([order_item.price for order_item in Order_Item.objects.filter(order=o)])
        print(o.payment)
    content['orders'] = orders

    # print(products_temp)
    return render(request, 'account/account-orders.html', content)


@login_required(login_url='/login/')
def get_user_account_order(request, order_id):
    content = {}
    try:
        order = Order.objects.get(id=order_id)

    except ObjectDoesNotExist:
        order = None
    if order is not None:
        content['order_items'] = Order_Item.objects.filter(order=order)
    else:
        content['error'] = f"We couldn't fine Order no. {order_id}"
        return render(request, 'account/account-order-details.html', content)

    order.amount = sum([order_item.price for order_item in content['order_items']])
    # print("PRICE", sum([order_item.price for order_item in content['order_items']]))
    content['order'] = order

    return render(request, 'account/account-order-details.html', content)


@login_required(login_url='/login/')
def get_user_account(request):
    content = {'n': range(10)}
    return render(request, 'account/account-home.html', content)

