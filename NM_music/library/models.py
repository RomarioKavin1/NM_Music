from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f'{self.title} by {self.artist.name}'

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in seconds")

    def __str__(self):
        return self.title
