from rest_framework import serializers
from .models import Circle

class CircleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Circle
        fields = ('lat', 'lng', 'radius', 'resolution', 'id')
