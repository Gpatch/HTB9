import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="b2fdba42e5ea4b7c87ea12c68d850c62",
														   client_secret="its a secret"))


def getSongs(playlistURI):
	result = sp.playlist(playlistURI)

	tracks = result['tracks']
	items = tracks['items']

	uris = []
	for item in items:
		track = item['track']
		uri = track['uri']
		uris.append(uri)

	return uris


getSongs("37i9dQZEVXbMMy2roB9myp")
