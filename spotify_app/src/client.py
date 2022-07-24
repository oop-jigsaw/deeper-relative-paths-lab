import requests

client_id = "bf04c6adec91456bae56ed5675b34a3c"
client_secret = "89dd0d234ec6413589e71279b37adfa8"

def get_access_token(client_id, client_secret):
    grant_type = 'client_credentials'
    body_params = {'grant_type' : grant_type}
    url='https://accounts.spotify.com/api/token'
    response=requests.post(url, data=body_params, auth = (client_id, client_secret)) 
    token_resp = response.json()
    access_token = token_resp['access_token']
    return access_token

def make_request(token, url):
    headers = {"Authorization": f"Bearer {token}"}
    search_resp = requests.get(url, headers = headers).json()
    return search_resp