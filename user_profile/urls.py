from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path("<username>", views.get_user_profile, name="profile"),
]