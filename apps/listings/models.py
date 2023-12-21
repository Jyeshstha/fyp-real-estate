from django.contrib.gis.db import models


# from django.contrib.gis.geos import Point

# Create your models here.
class Listings(models.Model):
    location = models.PointField(blank=True, null=True, srid=4326)
