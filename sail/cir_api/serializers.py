from rest_framework import serializers
from django.core.serializers import serialize
from .models import Circle
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class CircleSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Circle
        fields = ('lat', 'lng', 'radius', 'resolution', 'id', 'polygon')
        geo_field = 'polygon'
