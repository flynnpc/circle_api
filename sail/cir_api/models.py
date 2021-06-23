from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Circle(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    radius = models.IntegerField()
    resolution = models.PositiveIntegerField(validators=[MinValueValidator(3)])
    id = models.CharField(max_length=6, primary_key=True)

    def __str__(self):
        return self.id
