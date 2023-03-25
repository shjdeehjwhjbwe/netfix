from django.db import models
import rest_framework
from .actor import Actor

class Movie(models.Model):
    THRILLER = 'thiller'
    SPORTS = 'sports'
    COMEDY = 'comedy'
    HORROR = 'horror'
    MELODY = 'melody'
    yyy = (
        (THRILLER , 'thiller'), (HORROR , 'horror'),
        (SPORTS , 'sports'), (MELODY , 'melody'),
        (COMEDY , 'comedy')
    )
    name = models.CharField(max_length=50 , blank=False , null= False)
    year = models.IntegerField(blank=False)
    imdb = models.IntegerField(blank=True)
    genre = models.CharField(choices=yyy , max_length=400, blank=False)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name