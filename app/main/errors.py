"""App Http Errors

Declaration of App's Http errors
to send back to users making calls
to app endpoints
"""
# pylint: disable=invalid-name, redefined-builtin
def bad_request(message, id=""):
    """Bad Request http error template"""
    return {'error': 'bad request', 'id': id, 'message': message}, 400


def unauthorized(message, id=""):
    """Unauthorized http error template"""
    return {'error': 'unauthorized', 'id': id, 'message': message}, 401


def forbidden(message, id=""):
    """Forbidden http error template"""
    return {'error': 'forbidden', 'id': id, 'message': message}, 403


def not_acceptable(message, id=""):
    """Not Acceptable http error template"""
    return {'error': 'not acceptable', 'id': id, 'message': message}, 406
