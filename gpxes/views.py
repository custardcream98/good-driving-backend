from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from config.parser import GpxParser
from gpxes.apis.serializers import LineSerializer
import gpxes.models as gpx_models
from django.contrib.gis.db import models as geom_models
import gpxpy


class UploadGPX(APIView):

    """ Testing GPX POST API """

    parser_classes = [GpxParser]

    def post(self, request):
        print(request.data)

        # print(gpxpy.mod_gpx.GPX(request.data).)
        # line_serialized = LineSerializer(data={"geom": request.data})
        # if line_serialized.is_valid():
        #     # line_serialized.save()
        #     print(request.data)

        return Response(status=HTTP_200_OK)
