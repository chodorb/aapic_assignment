import tempfile
import csv
import os
import requests

from django.conf import settings
from celery import shared_task

from events.models import Event


@shared_task
def export_events(webhook_url):
    events = Event.objects.all()
    
    f = tempfile.NamedTemporaryFile(delete=False,suffix='.csv')
    
    fieldnames = ['id','name','start','end']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for event in events:
        writer.writerow({
            'id':event.id,
            'name':event.name,
            'start':event.start,
            'end':event.end
        })
    f.close()
    
    requests.post(webhook_url, json={'url':"lol"})
        
    