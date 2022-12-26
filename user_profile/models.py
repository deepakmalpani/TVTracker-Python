from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
from movie_details.models import Movie
from PIL import Image

def user_directory_path(instance, filename):
	profile_pic_name = 'profile_pictures/user_{0}/profile.jpg'.format(instance.user.id)
	full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

	if os.path.exists(full_path):
		os.remove(full_path)
	return profile_pic_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField( upload_to=user_directory_path, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    watching_movies = models.ManyToManyField(Movie, related_name='watching')
    planned_movies = models.ManyToManyField(Movie, related_name='planned')
    completed_movies = models.ManyToManyField(Movie, related_name='completed')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250,250
        if self.profile_pic:
            pic = Image.open(self.profile_pic.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.profile_pic.path)