import environ
import requests

env = environ.Env()
environ.Env.read_env()

class DeezerController:
    base_url = "https://api.deezer.com/"
    KEY = env("API_KEY")
    HOST = env("API_HOST")

    headers = {
	"x-rapidapi-key": KEY,
	"x-rapidapi-host": HOST
    }   

    def get_artist(self, artist_name):
        url = f"{self.base_url}/search/artist?q={artist_name}"
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                artist_data = response.json()
                if artist_data['data']:
                    artist = artist_data['data'][0]
                    return {
                        'id': artist['id'],
                        'name': artist['name'],
                        'num_albums': artist['nb_album'],
                        'picture': artist['picture']
                    }
                else:
                    return f"No artist found for {artist_name}"
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return e

    def get_artist_albums(self, artist_id):
        url = f"{self.base_url}artist/{artist_id}/albums"
        #url = f"https://api.deezer.com/artist/{artist_id}/albums"
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                albums = response.json()['data']
                full_length_albums = []
                for album in albums:
                    title = album['title'].lower()
                    if "deluxe" not in title and \
                    "remaster" not in title and \
                    "re-release" not in title and \
                    "alternate" not in title and \
                    "edition" not in title and \
                    "live" not in title and \
                    "(live)" not in title and \
                    "instrumental" not in title and \
                    "compilation" not in title and \
                    "greatest hits" not in title and \
                    "anthology" not in title and \
                    album['record_type'] == 'album':
                        if album['record_type'] == 'album':  # Filter only full-length albums
                            full_length_albums.append({
                                'id': album['id'],
                                'title': album['title'],
                                'cover': album.get('cover', 'No cover available'),
                                'num_tracks': album.get('nb_tracks', 'Unknown'),  # Default if missing
                                'run_time': album.get('duration', 'Unknown'),  # Default if missing
                                'release_date': album.get('release_date', 'Unknown')
                            })
                return full_length_albums
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return e

    def get_album_songs(self, album_id):
        url = f"{self.base_url}/album/{album_id}/tracks"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                songs = response.json()['data']
                filtered_songs = []
                for song in songs:
                    filtered_songs.append({
                        'id': song['id'],
                        'title': song['title'],
                        'run_ti me': song['duration']  # In seconds
                    })
                return filtered_songs
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return e
