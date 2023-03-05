from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    uri = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=150, null=True)
    acousticness = models.FloatField(null=True)
    danceability = models.FloatField(null=True)
    duration_ms = models.IntegerField(null=True)
    energy = models.FloatField(null=True)
    instrumentalness = models.FloatField(null=True)
    key = models.IntegerField(null=True)
    liveness = models.FloatField(null=True)
    loudness = models.FloatField(null=True)
    mode = models.IntegerField(choices=((0, "Minor"), (1, "Major")), null=True)
    speechiness = models.FloatField(null=True)
    tempo = models.FloatField(null=True)
    time_signature = models.IntegerField(null=True)
    valence = models.FloatField(null=True)

    def get_features(self):
        return (
            "acousticness", "danceability","duration_ms",
            "energy", "instrumentalness", "key",
            "liveness", "loudness", "mode",
            "speechiness", "tempo", "time_signature",
            "valence"
            )
        
    def __str__(self):
        return self.name


class Playlist(models.Model):
    PLAYLIST_CATEGORIES = (
        ("DAILY", "Top 50 daily"),
        ("WEEKLY", "Top 50 weekly"),    # popular right now
        ("VIRAL", "Top 50 viral"),      # becoming popular
    )

    uri = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=PLAYLIST_CATEGORIES)
    title = models.CharField(max_length=120)
    songs = models.ManyToManyField(Song, through='SongInPlaylist')
    date = models.DateField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} {self.date}"


class SongInPlaylist(models.Model):
    playlist = models.ForeignKey(to=Playlist, on_delete=models.SET_NULL, null=True, related_name="listings")
    song = models.ForeignKey(to=Song, on_delete=models.SET_NULL, null=True, related_name="listings")
    position = models.IntegerField()
