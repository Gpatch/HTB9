import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="b2fdba42e5ea4b7c87ea12c68d850c62",
														   client_secret="32fda940160c49c0a0989b336eb9f79b"))


def getSongs(playlistURI):
	result = sp.playlist(playlistURI)

	tracks = result['tracks']
	items = tracks['items']

	uris = []
	for item in items:
		track = item['track']
		uri = track['uri']
		uris.append(uri)

	# print(uris)
	return uris


getSongs("37i9dQZEVXbMMy2roB9myp")
