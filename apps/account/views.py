from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.order.models import Order, Order_Item
from apps.authentication.models import Address, User_Address, User
from django.core.exceptions import ObjectDoesNotExist
from apps.order.views import is_ajax
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers


@login_required(login_url='/login/')
def get_user_account_orders(request):
    content = {}

    orders = Order.objects.filter(user=request.user)
    content['orders'] = orders

    # print(products_temp)
    return render(request, 'account/account-orders.html', content)


@login_required(login_url='/login/')
def get_user_account_order(request, order_id):
    content = {}
    try:
        order = Order.objects.get(id=order_id, user=request.user.id)

    except ObjectDoesNotExist:
        order = None
    if order is not None:
        content['order_items'] = Order_Item.objects.filter(order=order)
    else:
        content['error'] = f"We couldn't fine Order no. {order_id}"
        return render(request, 'order/order-details.html', content)

    content['order'] = order

    return render(request, 'order/order-details.html', content)


@login_required(login_url='/login/')
def get_user_saved_addresses(request):
    content = {}
    try:
        # addresses = Address.objects.filter(id__in=User_Address.objects.values_list('address_id', flat=True).filter(user=request.user.id))
        addresses = User_Address.objects.filter(user=request.user.id)
    except ObjectDoesNotExist:
        addresses = None
        error_message = 'You do not have any saved address yet'

    content['addresses'] = addresses

    return render(request, 'account/account-saved-addresses.html', content)


@login_required(login_url='/login/')
def get_user_account(request):
    content = {'n': range(10)}
    return render(request, 'account/account-home.html', content)


@login_required(login_url='/login/')
def get_user_addresses(request):
    content = {}
    if is_ajax(request):
        # user_addresses =
        addresses = [address.address for address in
                     User_Address.objects.filter(user=User.objects.get(id=request.GET.get("user_id", None))).only(
                         'address')]
        # for user_address in user_addresses:
        #     # addresses.append(Address.objects.get(id=user_address.address.id))
        #     addresses.append(user_address.address)
        print("ADD", [a for a in addresses])
        content['addresses'] = addresses
        return render(request, 'modal/cart-addresses.html', content)


@login_required(login_url='/login/')
def choose_address(request):
    content = {}
    if is_ajax(request):
        try:
            user = User.objects.get(id=request.user.id)
            user.last_used_address = Address.objects.get(id=request.GET.get("address_id", None))
            user.save()
            # content['address'] = user.last_used_address
            data = serializers.serialize("json", [user.last_used_address])
            content['address'] = data
            return JsonResponse(content, status=200)
        except ObjectDoesNotExist:
            return JsonResponse(content, status=400)

    return JsonResponse(content, status=400)


@login_required(login_url='/login/')
def save_address(request):
    content = {}
    if is_ajax(request):
        try:
            name = request.GET.get("name")
            address = request.GET.get("address")
            postal_code = request.GET.get("postal_code")
            city = request.GET.get("city")
            country = request.GET.get("country")

            user = User.objects.get(id=request.user.id)
            new_address = Address(address=address, postal_code=postal_code,
                                  city=city, country=country)
            new_address.save()

            address_rel = User_Address(name=name, address=new_address, user=user)
            address_rel.save()

            user.last_used_address = new_address
            user.save()

            data = serializers.serialize("json", [user.last_used_address])
            content['address'] = data
            return JsonResponse(content, status=200)
        except Exception as e:
            print(f"Error during saving address\n{e}")
            return JsonResponse(content, status=400)

    return JsonResponse(content, status=400)
