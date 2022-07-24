def top_tracks_url(artist_name, token):
    artist = artist_search_url(artist_name, token)
    artist_id = artist['id']
    track_search = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US'
    track_resp = make_request(token, track_search)
    track_info = extract_track_info(track_resp, keys = ['name', 'id', 'popularity'])
    return track_info

def extract_track_info(track_response, keys = ['name', 'id', 'popularity']):
    return {k:v for k, v in track_response.items() if k in keys}

def extract_tracks_info(tracks_response, keys = ['name', 'id', 'popularity']):
    return [extract_track_info(track_response, keys) for track_response in tracks_response]