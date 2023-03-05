from django.urls import path
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from api import views, models
import csv
import requests
from datetime import date
import os

features = [
    "acousticness", "danceability","duration_ms",
    "energy", "instrumentalness", "key",
    "liveness", "loudness", "mode",
    "speechiness", "tempo", "time_signature",
    "valence"
]
auth = "Bearer BQDkjz7y214Xzz2HCHMF1WAppEnhivsU6HPJt1ubx1roIqFsxxbLnZ2mXwZxf_lPRJum3N4WitkCbK-Iyh7VcQ62IBeJjR_NHV_4unfaOVbcpBPnHD3TSnC4k2HqPA6ashsuyz1DF8ZP03dOd22ApQi7NzaW89EtxffSJOs44Ge0yGqE94XEEBtHfGTcK7bNlWm9uSrMn482T4SVOk3AvICV40Vp"

router = DefaultRouter()
router.register('song', views.SongViewSet)
router.register('playlist', views.PlaylistViewset)
router.register('country', views.CountryViewSet)


def get_song_features(request):
    for playlist in models.Playlist.objects.all():
        country_name = playlist.title.split(' - ')[1]
        print(country_name)
        country = models.Country.objects.get(name=country_name)
        playlist.country = country
        playlist.save()
    # songs = models.Song.objects.all()
    # for song in songs:
    #     try:
    #         print(song)
    #         features_data = requests.get("https://api.spotify.com/v1/audio-features/" + song.uri, headers={"Authorization": auth}).json()
    #         for feature in features:
    #             setattr(song, feature, features_data[feature])
    #         song.save()
    #     except Exception as e:
    #         print(e)
    return HttpResponse()


def populate(request):
    today = date.today()
    with open('countries.csv') as playlists:
        reader = csv.reader(playlists)
        labels = next(reader)
        for row in reader:
            country, daily, viral, weekly = row
            for playlist, category in zip([daily, viral, weekly], labels[1:]):
                try:
                    url = "https://api.spotify.com/v1" + playlist.replace("playlist", "playlists")
                    resp = requests.get(url, headers={"Authorization": auth})
                    data = resp.json()
                    
                    name = data["name"]
                    p_id = data["id"]
                    try:
                        playlist_obj = models.Playlist.objects.get(uri=p_id, date=today)
                    except models.Playlist.DoesNotExist:
                        playlist_obj = models.Playlist.objects.create(uri=p_id)
                        playlist_obj.title = name
                        playlist_obj.category = category
                    
                    for position, track in enumerate(data["tracks"]["items"]):
                        s_id = track["track"]["id"]
                        s_name = track["track"]["name"]
                        try:
                            song = models.Song.objects.get(uri=s_id)
                        except models.Song.DoesNotExist:
                            song = models.Song.objects.create(uri=s_id)
                            song.name = s_name

                        song.save()

                        models.SongInPlaylist.objects.get(playlist=playlist_obj, song=song, position=position)

                    playlist_obj.save()
                except Exception as e:
                    print(country, playlist, category)
                    print(e)
    return HttpResponse()

urlpatterns = [
    path('populate/', populate),
    path('features/', get_song_features)
] + router.urls
