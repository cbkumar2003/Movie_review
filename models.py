from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class todoitem_movie(models.Model): 
    movie_name = models.CharField(max_length=200) 
    movie_language = models.CharField(max_length=200)
    movie_rate = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    movie_review = models.CharField(max_length=2000)
    movie_watched = models.BooleanField(default=True)

    def __str__(self):
        return self.movie_name
