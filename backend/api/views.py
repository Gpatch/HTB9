from django.shortcuts import render
from django.db.models import Avg, Max, Min
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from api.models import Song, Playlist, Country
from api.serializers import SongSerializer, PlaylistSerializer, CountrySerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self, request, *args, **kwargs):
        mode = self.request.query_params.get('mode')
        features = self.request.query_params.get('features')
        countries = Country.objects.all()
        data = []
        # x - min / d
        for playlist in Playlist.objects.filter(category=mode.upper()):
            if playlist.country.name == "Global":
                continue
            if playlist.country.name == "Hong Kong":
                p_data = ["China"]
            else:
                p_data = [playlist.country.name]
            
            for feature in features.split(','):
                q_set = playlist.songs.all().aggregate(average=Avg(feature))
                avg = q_set["average"]
                # avg = (q_set["average"] - q_set["minimum"]) / (q_set["maximum"] - q_set["minimum"])
                # data[playlist.country.name][feature] = q_set["average"]
                p_data.append(avg)
            
            if playlist.country.name == "Kazakhstan":
                data.append(["Russia", *p_data[1:]])
            data.append(p_data)

        return Response(data=data)


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PlaylistViewset(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def list(self, request, *args, **kwargs):

        return Response(data={})

    def retrieve(self, request, *args, **kwargs):
        playlist = self.get_object()
        # serializer = self.get_serializer(instance)
        features = self.request.query_params.get('feature')
        data = {}
        for feature in features.split(','):
            q_set = playlist.songs.all().aggregate(average=Avg(feature))
            data[feature] = q_set["average"]
            # print(feature, playlist.listings.all().aggregate(Avg(feature)))
            # data[feature] = map(lambda song: getattr(song, feature), playlist.songs)
        return Response(data=data)

