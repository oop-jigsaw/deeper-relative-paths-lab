


def artist_search_url(artist_name, token):
    artist_search = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist"
    search_resp = make_request(token, artist_search)
    artist_info = extract_artist_info(search_resp)
    return artist_info

def extract_artist_info(search_resp):
    first_artist = search_resp['artists']['items'][0]
    return {'name': first_artist['name'], 'id': first_artist['id'],
            'popularity': first_artist['popularity']}