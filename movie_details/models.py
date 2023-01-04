from django.db import models

# Create your models here.
class Movie(models.Model):
    Title = models.CharField(max_length=255)
    Year = models.CharField(max_length=25, blank=True)
    Rated = models.CharField(max_length=10,blank=True)
    Genre = models.CharField(max_length=255, blank=True)
    Director = models.CharField(max_length=100, blank=True)
    Actors = models.CharField(max_length=255, blank=True)
    Plot = models.CharField(max_length=900, blank=True)
    imdbID = models.CharField(max_length=10, blank=True)
    Type = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return self.Title
