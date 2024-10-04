from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=100)
    def __str__(self):
        return self.genre


class MovieBrowse(models.Model):
    name = models.CharField(max_length=100)
    releaseDate = models.DateField()
    metacriticScore = models.IntegerField()
    reviews = models.TextField(blank=True)
    embedLink = models.CharField(max_length=500, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    def __str__(self):
        return self.name




