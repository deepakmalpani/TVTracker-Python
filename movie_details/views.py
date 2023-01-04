from django.shortcuts import render
from .models import Movie
from user_profile.models import Profile
import environ
import requests
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

env = environ.Env()
# reading .env file
environ.Env.read_env()

API_KEY = env("API_KEY")
# Create your views here.

def get_movie_details(request, imdb_id):
    if Movie.objects.filter(imdbID = imdb_id).exists():
        movie_data = Movie.objects.get(imdbID = imdb_id)
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
                imdbID = movie_data['imdbID'],
            )
            m.save()
        db_cache = False
    
    context = {
            'movie_data' : movie_data,
            'db_cache' : db_cache
        }
    template = loader.get_template('movie_details.html')

    return HttpResponse(template.render(context, request))

def add_movies_planned(request, imdb_id):
    movie = Movie.objects.get(imdbID = imdb_id)
    user = request.user
    profile = Profile.objects.get(user = user)
    
    profile.planned_movies.add(movie)

    return HttpResponseRedirect(reverse('movie_details:movie-details', args = [imdb_id]))

def add_movies_watching(request, imdb_id):
    movie = Movie.objects.get(imdbID = imdb_id)
    user = request.user
    profile = Profile.objects.get(user = user)

    if profile.planned_movies.filter(imdbID = imdb_id).exists():
        profile.planned_movies.remove(movie)

    profile.watching_movies.add(movie)

    return HttpResponseRedirect(reverse('movie_details:movie-details', args = [imdb_id]))

def add_movies_completed(request, imdb_id):
    movie = Movie.objects.get(imdbID = imdb_id)
    user = request.user
    profile = Profile.objects.get(user = user)

    if profile.watching_movies.filter(imdbID = imdb_id).exists():
        profile.watching_movies.remove(movie)
    
    if profile.planned_movies.filter(imdbID = imdb_id).exists():
        profile.planned_movies.remove(movie)

    profile.completed_movies.add(movie)

    return HttpResponseRedirect(reverse('movie_details:movie-details', args = [imdb_id]))


