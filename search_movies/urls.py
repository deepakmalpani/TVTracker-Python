from django.urls import path
from . import views
from .views import HomePageView
from movie_details.views import get_movie_details

urlpatterns = [
    path("search/", views.search_results, name="search_results"),
    path("",HomePageView.as_view(), name="home"),
    path("<imdb_id>", get_movie_details, name='movie-details')
]