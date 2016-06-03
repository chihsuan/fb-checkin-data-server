from django.db import models
from datetime import datetime

class Place(models.Model):
    category = models.CharField(max_length=64)
    category_list_id = models.CharField(max_length=16)
    category_list_name = models.CharField(max_length=64)
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=16)
    state = models.CharField(max_length=16)
    country = models.CharField(max_length=16)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(db_index=True, max_length=128)
    pageUrl = models.TextField(default='')
    place_id = models.CharField(db_index=True, max_length=16)
    place_zip = models.CharField(max_length=16)

class Checkin(models.Model):
    visit = models.IntegerField()
    date = models.DateField(default=datetime.now)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

class Like(models.Model):
    like = models.IntegerField()
    date = models.DateField(default=datetime.now)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
