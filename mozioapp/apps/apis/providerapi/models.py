from django.db import models
from mongoengine import *


class Providers(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_no = models.CharField(max_length=20)
    language = models.CharField(max_length=2)# ISO 639-1 Language code
    currency = models.CharField(max_length=3)# ISO 4217 Currency code
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created'
        db_table = 'providers'

    def __unicode__(self):
        return self.name


class ServiceArea(Document):
    meta = {'collection': 'service_area'}
    provider_id = StringField(required=True)
    polygon = PolygonField(required=True)  # GeoJSON
    name = StringField(required=True)
    price = StringField(required=True)
    is_active = BooleanField(default=True)

    def __unicode__(self):
        return self.name
