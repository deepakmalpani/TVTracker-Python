from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def get_user_profile(request, username):
    user = get_object_or_404(User, username = username)
    profile = Profile.objects.get(user = user)

    movies_completed_count = profile.completed_movies.count()
    movies_watching_count = profile.watching_movies.count()
    movies_planned_count = profile.planned_movies.count()

    context = {
        'profile' : profile,
        'movies_completed_count' : movies_completed_count,
        'movies_watching_count' : movies_watching_count,
        'movies_planned_count' : movies_planned_count
    }

    template = loader.get_template('profile.html')

    return HttpResponse(template.render(context,request))
