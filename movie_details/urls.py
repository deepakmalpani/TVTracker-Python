from django.urls import path
from . import views

app_name = 'movie_details'
urlpatterns = [
    path("<imdb_id>", views.get_movie_details, name='movie-details')
]