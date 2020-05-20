"""Custom Response

Declaration of Custom Response
"""
# pylint: disable=too-few-public-methods
from flask import jsonify, Response


class MyResponse(Response):
    """Custom Response

    To avoid repeating code on every Response,
    related to a new token available different
    from the one used to make the requesr, and
    by default set content type as json
    """
    default_mimetype = 'application/json'

    @classmethod
    def force_type(cls, response_value, environ=None):
        """Whenever we receive a dictionary we jsonify the response,
        but also verify if there's a new api_key available to send
        back to client
        """
        if isinstance(response_value, dict):
            response_value = jsonify(response_value)
        return super(MyResponse, cls).force_type(response_value, environ)
