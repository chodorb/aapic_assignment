from django.db import models

class Artist(models.Model):
    name = models.CharField(unique=True, max_length=255)
    
    GENRE_CHOICES = (
        ("rap","rap"),
        ("pop","pop"),
        ("rock","rock"),
    )
    music_genre = models.CharField(max_length=255, choices=GENRE_CHOICES)
    
    def __str__(self):
        return self.name
