from rest_framework import serializers
from gpxes import models as gpx_models


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = gpx_models.Line
        fields = '__all__'
