from src.client import *


def artist_search_url(artist_name, token):
    artist_search = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist"
    return artist_search

def extract_artist_info(search_resp):
    first_artist = search_resp['artists']['items'][0]
    return {'name': first_artist['name'], 'id': first_artist['id'],
            'popularity': first_artist['popularity']}

def get_artist(artist_name, token):
    artist_search = artist_search_url(artist_name, token)
    search_resp = make_request(token, artist_search)
    artist_info = extract_artist_info(search_resp)
    return artist_info