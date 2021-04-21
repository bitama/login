from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("users/register",views.register_user),
    path("user/login",views.user_login),
    path("user/success", views.user_success),
    path("user/logout",views.user_logout)
]