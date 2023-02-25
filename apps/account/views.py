from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def get_user_account_orders(request):
    content = {'n': range(10)}

    # print(products_temp)
    return render(request, 'account/account-orders.html', content)


@login_required(login_url='/login/')
def get_user_account(request):
    content = {'n': range(10)}
    return render(request, 'account/account-home.html', content)

