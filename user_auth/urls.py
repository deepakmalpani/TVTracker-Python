from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path("register", views.create_new_user, name="register"),
    path("login",views.login_user, name="login"),
    path("logout",views.logout_user, name = "logout")
]