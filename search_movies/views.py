from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

API_KEY = env("API_KEY")

# Create your views here.


def search_results(request):
    query = request.GET.get("q")
    url = 'http://www.omdbapi.com/?apikey='+API_KEY+'&s=' + query
    response = requests.get(url)
    movie_data = response.json()
    # return movie_data
    # return render(request,"search_results.html" , {'movie_data': movie_data['Search']})
    context = {
        'query' : query,
        'movie_data' : movie_data,
        'page_number' : 1,
    }

    template = loader.get_template('search_results.html')

    return HttpResponse(template.render(context,request))


    