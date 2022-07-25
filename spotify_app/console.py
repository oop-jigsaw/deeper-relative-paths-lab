

token = get_access_token(client_id, client_secret)

paul_simon_request_url = artist_search_url('paul simon', token)
paul_simon_data = make_request(token, paul_simon_request_url)
paul_simon_info = extract_artist_info(paul_simon_data)

simon_id = paul_simon_info['id']

simon_artist_url = top_tracks_url(simon_id, token)


simon_tracks = make_request(token, simon_artist_url)
tracks = simon_tracks['tracks']

first_track = tracks[0]
top_songs_info = extract_tracks_info(simon_tracks['tracks'])


top_song_id = top_songs_info[0]['id']


audio_url = audio_features(top_song_id)

audio_data = make_request(token, audio_url)

extracted_audio = extract_audio_data(audio_data, selected_attrs = ['danceability', 'energy', 'loudness', 'instrumentalness'])
artist_name = 'paul simon'

paul_simon_data = get_artist(artist_name, token)

top_tracks_info = get_top_tracks(artist_name, token)