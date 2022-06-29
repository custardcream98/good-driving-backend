from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from config.parser import GpxParser
from gpxes.apis.serializers import LineSerializer, PointSerializer
from django.contrib.gis.geos import Point
import gpxpy


class UploadGPX(APIView):

    """ Testing GPX POST API """

    parser_classes = [GpxParser]

    def post(self, request):
        data: gpxpy.mod_gpx.GPX = request.data
        points = data.get_points_data(
            distance_2d=True)

        for p in points:
            print(f'{p.point.latitude} {p.point.longitude}')
            print(p.point.time)
            line_serialized = PointSerializer(
                data={"geom": Point(x=p.point.longitude, y=p.point.latitude, srid=4326),
                      "time": p.point.time})
            if line_serialized.is_valid():
                line_serialized.save()

        return Response(data={"status": "All Green"}, status=HTTP_200_OK)
