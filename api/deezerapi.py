import environ
import requests

env = environ.Env()
environ.Env.read_env()

class DeezerAPI:
    base_url = "https://api.deezer.com/"
    KEY = env("API_KEY")
    HOST = env("API_HOST")

    def get_user_id(self):
        pass

    def get_user_data(self):
        pass

    def get_user_albums(self):
        pass

    def get_album_songs(self):
        pass
