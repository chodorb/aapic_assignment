from django.db import models
from events.models import Event
from artists.models import Artist


class Performance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    artists = models.ManyToManyField(Artist)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f'{self.event.name} - {self.start_time} to {self.end_time}'