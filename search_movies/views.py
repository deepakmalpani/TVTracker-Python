from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

API_KEY = env("API_KEY")

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

def search_results(request):
    query = request.GET.get("q")
    url = 'http://www.omdbapi.com/?apikey='+API_KEY+'&s=' + query
    response = requests.get(url)
    movie_data = response.json()
    # return movie_data
    return render(request,"search_results.html" , {'movie_data': movie_data['Search']})

