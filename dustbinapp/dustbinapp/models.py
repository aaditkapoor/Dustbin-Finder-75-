from django.db import models


class DustBin(models.Model):
    lat = models.CharField(max_length=100)
    lon = models.CharField(max_length=100)


    def __unicode__(self):
        return self.lat + " " + self.lon
