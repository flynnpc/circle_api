# from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import math
import decimal


# Create your models here.
class Circle(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    radius = models.DecimalField(max_digits=14, decimal_places=8)
    resolution = models.PositiveIntegerField(validators=[MinValueValidator(3)])
    id = models.CharField(max_length=6, primary_key=True)
    polygon = models.PolygonField(null=True, default=None)

    @property
    def polygon(self):
        coords = []
        angle = decimal.Decimal(2 * math.pi / self.resolution)
        for point in range(self.resolution):
            coords.append((self.lng + self.radius * decimal.Decimal(math.sin(point * angle)),
                          self.lat + self.radius * decimal.Decimal(math.cos(point * angle))
                          ))
        return coords

    def __str__(self):
        return self.id
