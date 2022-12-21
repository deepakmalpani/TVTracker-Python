from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['Title','Year']

admin.site.register(Movie, MovieAdmin)
# Register your models here.
