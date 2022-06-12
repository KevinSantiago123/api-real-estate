from estate_habi.models.estate_habi_model import OperationDB
from server.response import Response

def get_estate_view(request):
    """Get all the real estate"""
    try:
        #print(request.query_params)
        operations_query = OperationDB()
        data = operations_query.get_all_property()
        if len(data) > 0:
            return Response.status(200, info=data)
        return Response.status(404)
    except Exception as error:
        return Response.status(500)
