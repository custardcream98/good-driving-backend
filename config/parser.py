from rest_framework.parsers import BaseParser
import gpxpy


class GpxParser(BaseParser):
    """
    Custom GPX parser.
    """
    media_type = 'application/xml'

    def parse(self, stream, media_type=None, parser_context=None):
        return gpxpy.parse(stream.read())
