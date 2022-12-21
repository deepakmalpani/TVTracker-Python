from django.shortcuts import render
from .models import Movie
import environ
import requests
from django.template import loader
from django.http import HttpResponse

env = environ.Env()
# reading .env file
environ.Env.read_env()

API_KEY = env("API_KEY")
# Create your views here.

def get_movie_details(request, imdb_id):
    if Movie.objects.filter(ImdbId = imdb_id).exists():
        movie_data = Movie.objects.get(ImdbId = imdb_id)
        db_cache = True

        
    else:
        url = 'http://www.omdbapi.com/?apikey='+API_KEY+'&i=' + imdb_id
        response = requests.get(url)
        movie_data = response.json()

        if movie_data['Type'] == 'movie':
            m, created = Movie.objects.get_or_create(
                Title = movie_data['Title'],
                Year = movie_data['Year'],
                Rated = movie_data['Rated'],
                Genre = movie_data['Genre'],
                Director = movie_data['Director'],
                Actors = movie_data['Actors'],
                Plot = movie_data['Plot'],
                ImdbId = movie_data['imdbID'],
            )
            m.save()
        db_cache = False
    
    context = {
            'movie_data' : movie_data,
            'db_cache' : db_cache
        }
    template = loader.get_template('movie_details.html')

    return HttpResponse(template.render(context, request))
    
