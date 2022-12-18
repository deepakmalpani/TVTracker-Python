from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path("search/", views.search_results, name="search_results"),
    path("",HomePageView.as_view(), name="home")
]