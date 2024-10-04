from django.db import models

class Artist(models.Model):
    id = models.IntegerField(null=False)
    num_albums = models.IntegerField(null=False)
    name = models.CharField(max_length=50)
    picture = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_id(self):
        return self.id

class Album(models.Model):
    id = models.IntegerField(null=False)
    run_time = models.IntegerField(null=True)
    num_tracks = models.IntegerField(null=False)
    title = models.CharField(max_length=50, null=False)
    release_date = models.TextField(null=False)
    cover = models.TextField(blank=True, null=True)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} from artist {self.artist.name}"
    
    def get_id(self):
        return self.id
    
class Song(models.Model):
    id = models.IntegerField(null=False)
    run_time = models.IntegerField(null=True)
    title = models.CharField(max_length=50)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} from album {self.album.name} by {self.album.artist.name}"
    
    def get_id(self):
        return self.id