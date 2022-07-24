def audio_features(track_id):
    base_url = 'https://api.spotify.com'
    features = f'/v1/audio-features/{track_id}'
    return f'{base_url}{features}'

def extract_audio_data(audio_data, selected_attrs = ['danceability', 'energy', 'loudness', 
                      'speechiness', 'acousticness', 
                      'instrumentalness', 'liveness', 'valence']):
    return {k:v for (k, v) in audio_data.items() if k in selected_attrs}
