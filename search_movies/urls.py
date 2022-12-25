from django.urls import path
from . import views

app_name = 'search_movies'

urlpatterns = [
    path("", views.search_results, name="search_results"),
]