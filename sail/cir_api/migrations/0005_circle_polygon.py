# Generated by Django 3.2.4 on 2021-06-25 21:37

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cir_api', '0004_alter_circle_radius'),
    ]

    operations = [
        migrations.AddField(
            model_name='circle',
            name='polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(default=None, null=True, srid=4326),
        ),
    ]
