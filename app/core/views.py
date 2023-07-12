"""
CORE VIEWS FOR APP.CORE
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health_check(request):
    return Response({"healthy": True})
