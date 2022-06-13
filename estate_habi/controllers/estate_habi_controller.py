from estate_habi.models.estate_habi_model import OperationDB, Validations
from server.response import Response

__author__ = 'kcastanedat'


class ControllerEstate:

    def get(self, request):
        """Validates the parameters and proceeds to list the data sought in the property"""
        try:
            # Validate request parameters
            if len(request.args) > 0:
                validations = Validations(request)
                if validations.request_is_not_valid():
                    return validations.errors()
                operations_query = OperationDB()
                data = operations_query.get_property_by_filter(
                    validations.request)
            # In the url there is no parameter
            else:
                operations_query = OperationDB()
                data = operations_query.get_all_property()
            if len(data) > 0:
                return Response.status(200, info=data)
            return Response.status(404)
        except Exception as e:
            print(e)
            return Response.status(500)
