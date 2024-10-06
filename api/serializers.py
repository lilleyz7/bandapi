from rest_framework import serializers
from .models import Artist, Album, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'run_time', 'album']

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    class Meta:
        model = Album
        fields = ['title', 'deezer_id', 'cover', 'num_tracks', 'run_time', 'release_date']

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'num_albums', 'picture', 'albums']

