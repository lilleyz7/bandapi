from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    id = models.IntegerField(null=False)
    name = models.CharField(max_length=50)
    picture = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    id = models.IntegerField(null=False)
    runtime = models.IntegerField(required=True)
    name = models.CharField(max_length=50)
    picture = models.TextField(blank=True, null=True)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} from artist {self.artist.name}"
    
class Song(models.Model):
    id = models.IntegerField(null=False)
    name = models.CharField(max_length=50)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} from album {self.album.name} by {self.album.artist.name}"