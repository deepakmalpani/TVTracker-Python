from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['Title','Year']

admin.site.register(Movie, MovieAdmin)
