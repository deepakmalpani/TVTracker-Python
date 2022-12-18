from django.db import models

# Create your models here.
class Movie(models.Model):
    Title = models.CharField(max_length=255)
    Year = models.CharField(max_length=25, blank=True)

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return self.name