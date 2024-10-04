from deezerapi import DeezerController

def test_api():
    controller = DeezerController()
    test_names = ["windir", "enslaved", "monolord"]
    total_errors = 0
    mishaps = 0
    artists = []
    albums = []
    songs = []
    for name in test_names:
        artist_details = controller.get_artist(name)
        if isinstance(artist_details, str):
            mishaps += 1
            print(f"{name} had a mishap and received: {artist_details}\n\n")
            print("-----------------------------------------")
        if isinstance(artist_details, Exception):
            total_errors += 1
            print(f"{name} failed and received: {artist_details}\n\n")
            print("-----------------------------------------")
        else:
            print(artist_details)
            artists.append(artist_details)
            print("-----------------------------------------")

    for artist in artists:
        id = artist['id']
        print(f"{id}: {artist['name']}")
        response = controller.get_artist_albums(id)
        if isinstance(response, str):
            mishaps += 1
            print(f"{name} had a mishap and received: {response}\n\n")
            print("-----------------------------------------")
        elif isinstance(response, Exception):
            total_errors += 1
            print(f"{name} failed and received: {response}\n\n")
            print("-----------------------------------------")
        elif isinstance(response, list):
            for a in response:
                print(a)
            print("-----------------------------------------")
        else:
            print("how did we get here")
    

test_api()