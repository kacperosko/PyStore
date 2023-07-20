from django.urls import path, re_path
import apps.store.views
from .views import login_view, register_user, register_complete, register_activating
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register-complete/', register_complete, name="logout"),
    path('register-activating/', register_activating, name="logout"),
]
