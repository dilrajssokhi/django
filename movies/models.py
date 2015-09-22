import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_director = models.CharField(max_length=200)
    movie_genre = models.TextField(max_length=400,default='')
    movie_99popularity = models.DecimalField(max_digits=3, decimal_places=1)
    movie_imdbscore = models.DecimalField(max_digits=2, decimal_places=1)
    entry_date = models.DateTimeField('date entered')
    def __unicode__(self):
        return self.movie_name
    def was_entered_recently(self):
        return self.entry_date >= timezone.now() - datetime.timedelta(days=1)
