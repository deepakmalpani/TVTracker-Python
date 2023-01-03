from django.urls import path
from . import views

app_name = 'movie_details'
urlpatterns = [
    path("<imdb_id>", views.get_movie_details, name='movie-details'),
    path("<imdb_id>/addmovietowatching", views.add_movies_watching, name = "add-movie-to-watching"),
    path("<imdb_id>/addmovietocompleted", views.add_movies_completed, name = "add-movie-to-completed")
]