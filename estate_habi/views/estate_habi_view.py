from estate_habi.controllers.estate_habi_controller import ControllerEstate
from server.response import Response

__author__ = 'kcastanedat'


def get_estate_view(request):
    """Get all the real estate"""
    try:
        controller = ControllerEstate()
        response = controller.get(request)
        return response
    except Exception as error:
        return Response.status(500)
