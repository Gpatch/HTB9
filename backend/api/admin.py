from django.contrib import admin
from api.models import Song, Playlist, SongInPlaylist, Country

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(SongInPlaylist)
admin.site.register(Country)
