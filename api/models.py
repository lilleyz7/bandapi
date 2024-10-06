from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=255)
    deezer_id = models.IntegerField(unique=True)
    num_albums = models.IntegerField()
    picture = models.URLField()

    def __str__(self):
        return self.name
    
    def get_id(self):
        return self.id
    
# class ArtistRelationship(models.Model):
    # id = models.IntegerField(null=False)
    # user = models.ForeignKey(User, related_name="user_relation", on_delete=models.CASCADE)
    # artist = models.ForeignKey(Artist, related_name="artist_relation", on_delete=models.CASCADE)

class Album(models.Model):
    title = models.CharField(max_length=255)
    deezer_id = models.IntegerField(unique=True)
    cover = models.URLField()
    num_tracks = models.IntegerField(null=True)
    run_time = models.IntegerField(null=True)  # Duration in seconds
    release_date = models.DateField(null=True)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} from artist {self.artist.name}"
    
    def get_id(self):
        return self.id
    
class Song(models.Model):
    deezer_id = models.IntegerField(null=False)
    run_time = models.IntegerField(null=True)
    title = models.CharField(max_length=50)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} from album {self.album.name} by {self.album.artist.name}"
    
    def get_id(self):
        return self.id