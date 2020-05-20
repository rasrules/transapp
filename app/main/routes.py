"""Main Routes

Declaration of Main Blueprint routes
"""
# pylint: disable=invalid-name
import logging
from flask import g, request
from app.main import bp
#from app.models import Permission
from app.exceptions import ValidationError
#from app.main.decorators import permission_required
from app.main.errors import bad_request
# from app import current_app


logger = logging.getLogger(__name__)


"""
##########################################Views##########################################
"""
@bp.errorhandler(ValidationError)
def validation_error(e):
    """Blueprint Validation error handler"""
    return bad_request(e.args[0], "MUN-777")


# ************************Endpoints************************
@bp.route('/translate', methods=['POST'])
def get_translation():
    """Get Translation
    /*TODO: finish get_translation docstring*/
    """
    result = None
    response = {}
    from app.service.words import get
    # check if we received a valid parameters
    data = request.get_json()
    try:
        value = data and data.get('word', "") or ""
        language = data and data.get('lang', "") or "en"
        result = get(
            value=value, language=language
        )
        logger.info(result)
        response.update({'data': result})
    except Exception as ve_err:
        message = str(ve_err)
        logger.error(
            "get_translation : %s ",
            message
        )
        return bad_request(message)

    return response, 200


@bp.route('/remove', methods=['POST'])
def remove_translation():
    """Remove Translation
    /*TODO: finish remove_translation docstring*/
    """
    result = None
    response = {}
    from app.service.words import remove
    # check if we received a valid parameters
    data = request.get_json()
    try:
        value = data and data.get('word', "") or ""
        language = data and data.get('lang', "") or "en"
        result = remove(
            value=value, language=language
        )
        logger.info(result)
        response.update({'data': result})
    except Exception as ve_err:
        message = str(ve_err)
        logger.error(
            "remove_translation : %s ",
            message
        )
        return bad_request(message)

    return response, 200


@bp.route('/add', methods=['POST'])
def create_translation():
    """Remove Translation
    /*TODO: finish create_translation docstring*/
    """
    result = None
    response = {}
    from app.service.words import create
    # check if we received a valid parameters
    data = request.get_json()
    try:
        value = data and data.get('word', "") or ""
        language = data and data.get('lang', "") or "en"
        translation = data and data.get('transl', "") or ""
        result = create(
            value=value, language=language,
            translation=translation
        )
        logger.info(result)
        response.update({'data': result})
    except Exception as ve_err:
        message = str(ve_err)
        logger.error(
            "remove_translation : %s ",
            message
        )
        return bad_request(message)

    return response, 201
