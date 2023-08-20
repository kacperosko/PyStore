from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import UserManager
from .forms import LoginForm, SignUpForm
from django.template import RequestContext
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/account')

    form = LoginForm(request.POST or None)
    message = ""

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/account")
            else:
                message = 'Incorrect email or password'
        else:
            message = 'Error during login'

    return render(request, "authentication/authentication-login.html", {"form": form, "message": message})


def register_user(request):
    error_msg = None

    if request.user.is_authenticated:
        return redirect('/account')

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            phone = form.cleaned_data.get("phone")
            raw_password = form.cleaned_data.get("password1")

            user = authenticate(email=email, password=raw_password, first_name=first_name, last_name=last_name,
                                phone=phone)

            login(request, user)
            request.session["new_registered_activating"] = True
            request.session["new_registered_complete"] = True
            return redirect("/register-activating")

        else:
            print(form.cleaned_data)
            error_msg = form.errors
    else:
        form = SignUpForm()

    return render(request, "authentication/authentication-register.html",
                  {"form": form, "error_msg": error_msg})


def register_complete(request):
    if request.session.get("new_registered_complete", False):
        del request.session["new_registered_complete"]
        return render(request, "authentication/authentication-register-complete.html", {})
    else:
        return redirect("/")


def register_activating(request):
    if request.session.get("new_registered_activating", False):
        del request.session["new_registered_activating"]
        return render(request, "authentication/authentication-register-activating.html", {})
    else:
        return redirect("/")
