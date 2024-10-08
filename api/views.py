from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Artist, Album
# from deezerapi import DeezerController
from .deezerapi import DeezerController
from .serializers import ArtistSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@authentication_classes([JWTAuthentication , SessionAuthentication])
@permission_classes([IsAuthenticated])
def artist_details(request, artist_name):
    try:
        artist = Artist.objects.get(name__iexact=artist_name)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    except Artist.DoesNotExist:
        controller = DeezerController()
        try:
            artist = controller.get_artist(artist_name)
            if isinstance(artist, str):
                return Response({
                    'error': 'artist not found'
            })
            else:
                artist_data, created = Artist.objects.get_or_create(
                    name=artist['name'],
                    deezer_id=artist['id'],
                    num_albums=artist['num_albums'],
                    picture=artist['picture']
                )
                if not created:
                    return Response({
                        'error': 'unable to add artist to database'
                    })
                try:
                    albums = controller.get_artist_albums(artist_data['deezer_id'])
                    if isinstance(albums, Exception):
                        return Response({
                            'error': albums
                        })
                    if isinstance(albums, str):
                        return Response({'error': albums})
                    else:
                        for album in albums:
                            Album.objects.create(
                                artist=artist_data,
                                title=album['title'],
                                deezer_id=album['id'],
                                cover=album.get('cover', ''),
                                num_tracks=album.get('nb_tracks'),
                                run_time=album.get('duration'),
                                release_date=album.get('release_date')
                            )
                    serializer = ArtistSerializer(artist_data)
                    if serializer.is_valid():
                        return Response(serializer.data)
                    else:
                        return Response({
                            'error': serializer.errors}
                          
                            )
                except Exception as e:
                    print(e)
                    return Response({'error': str(e)})
        except Exception as e:
            print(e)
            return Response(
                {
                    'error': str(e)
                }
            )