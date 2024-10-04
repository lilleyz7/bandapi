from rest_framework import serializers
from .models import Artist, Album, Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Artist
        fields = ['id', 'name', 'num_albums', 'picture']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Album
        fields = ['id', 'title', 'run_time', 'num_tracks', 'release_date', 'cover', 'artist']

class SongSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Song
        fields = ['id', 'title', 'run_time', 'album']
