__author__ = 'kcastanedat'


class Response:
    """Contains http status and custom responses for services"""
    status_values = {
        100: "",
        101: "",
        200: "Ok",
        201: "Data stored correctly.",
        202: "",
        203: "",
        204: "",
        205: "",
        206: "",
        207: "",
        208: "",
        226: "",
        300: "",
        301: "",
        302: "",
        303: "",
        304: "",
        305: "",
        306: "",
        307: "",
        308: "",
        400: "The information entered could not be processed.",
        401: "You are not authorized to continue.",
        402: "Payment required.",
        403: "",
        404: "The requested information was not found.",
        405: "",
        406: "",
        407: "",
        408: "",
        409: "Data already exists with the information entered.",
        410: "",
        411: "",
        412: "",
        413: "",
        414: "",
        415: "",
        416: "",
        417: "",
        418: "",
        422: "",
        423: "",
        424: "",
        426: "",
        428: "",
        429: "",
        431: "",
        451: "",
        500: "There was an error processing the request.",
        501: "",
        502: "",
        503: "",
        504: "",
        505: "",
        506: "",
        507: "",
        508: "",
        509: "",
        510: "",
        511: ""
    }

    @classmethod
    def status(self, status_type, description_error=None, info=None):
        """Generates the content and status of the service response"""
        self.response = {"status": status_type}
        if description_error != None:
            self.response['message'] = description_error
        else:
            self.response['message'] = self.status_values[status_type]
        if info != None:
            self.response['data'] = info
        return self.response
