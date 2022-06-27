from django.db import models
from django.contrib.gis.db import models as geom_models


class Point(models.Model):

    """ Testing GPX Point POST API """

    geom = geom_models.PointField(
        null=False, srid=4326
    )


class Line(models.Model):

    """ Testing GPX Line POST API """

    geom = geom_models.MultiLineStringField(
        null=False, srid=4326
    )
