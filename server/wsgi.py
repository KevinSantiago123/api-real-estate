import json

from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound

from .settings import PATH_AND_METHODS
class App:
    """Implements a WSGI application for managing your favorite movies."""

    def dispatch_request(self, request):
        """Dispatches the request."""
        print(request.path)
        print(request.method)
        if (
            request.path in PATH_AND_METHODS
            and PATH_AND_METHODS[request.path][0] == request.method
        ):
            result = PATH_AND_METHODS[request.path][1](request)
            return Response(
                json.dumps(result, sort_keys=True) if result else {},
                status = result.get('status'),
                content_type="application/json"
            )
        return NotFound()

    def wsgi_app(self, environ, start_response):
        """WSGI application that processes requests and returns responses."""
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        """The WSGI server calls this method as the WSGI application."""
        return self.wsgi_app(environ, start_response)