"""App Models

Declaration of App's Models

Defines the Database's Models or Objects related to the Models
for the mongodb dbms
"""
# pylint: disable=invalid-name, import-outside-toplevel, too-few-public-methods
import logging
import mongoengine
from bson.objectid import ObjectId
from app.util import validate_string


logger = logging.getLogger(__name__)


# #####################CONSTANTS##############################

VALID_LANGUAGES = {
    'en': 'english', 'es': 'spanish'
}


def _clean_tags(tags, valid_chars="[^a-z0-9. -/]"):
    """Cleaning tags received befores saving them"""
    if not tags:
        return None
    #lower case only
    tags = list(map(lambda tag: tag.lower(), tags))
    #first remove repeated data
    tags = list(dict.fromkeys(tags))
    # now clean tag values
    tags = list(map(lambda tag: validate_string(tag, valid_chars), tags))
    return tags


def _not_valid_language(val):
    """Validates val against VALID_LANGUAGE"""
    if val and val not in  VALID_LANGUAGES:
        from mongoengine.errors import  ValidationError
        raise ValidationError('Not a valid language choice')


class Word(mongoengine.Document):
    value = mongoengine.StringField(unique=True, max_length=50)
    language = mongoengine.StringField(
        max_length=2, default="en", validation=_not_valid_language
    )
    translations = mongoengine.ListField(
        mongoengine.StringField(max_length=50),
        default=[]
    )
