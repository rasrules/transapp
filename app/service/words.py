"""Main Service Library for Word Model

Declaration of Main Service Support Library for Word Model
"""
# pylint: disable=invalid-name,import-outside-toplevel,consider-using-ternary,wrong-import-position
import logging
from mongoengine.errors import LookUpError
from app.models import Word
from app.util import validate_string
from app.exceptions import (
    ParameterExpected
)
from app.util import check_spelling
# from app import current_app


logger = logging.getLogger(__name__)

"""
##########################################WordHelpers##########################################
"""


def get(value: str, language, all_translations=False):
    """Returns the User instance, with its token
    only, by searching it by its email
    """

    try:
        if not check_spelling(value, language):
            raise ParameterExpected("Misspelled word provided!")
    except ValueError as ve_err:
        logger.error("Error while checking spell word : %s", str(ve_err))
        raise ParameterExpected("Invalid language provided!")

    result = None
    try:
        word_translations = Word.objects(value=value, language= language).only('translations').first()
        # translations contains only the first translation
        logger.info(str(word_translations))
        translations = None
        if word_translations:
            translations = list(word_translations.translations)
            logger.info(str(translations))
            if not all_translations:
                translations = [translations[0]]

        result = translations
        logger.info(str(result))
    except LookUpError as lue_err:
        logger.error("Error while getting word : %s", str(lue_err))
    except TypeError as te_err:
        logger.error("Error while getting word : %s", str(te_err))

        # pass
    return result


def create(value, language, translation):
    """Create Word/add translation to existing word for App

    It creates a valid Word for the app. If the word exists,
    it will add the new translation to the word's translations. If it doens't
    it will create a new Word with the translation provided
    """
    if not check_spelling(value, language):
        raise ParameterExpected("Misspelled word provided!")

    result = None
    try:
        value = validate_string(value, "[^a-z]")
        valid_word = Word.objects(value=value, language=language).first()
        #word already exist so let's add a new translation
        if not valid_word:
            valid_word = Word(
                value=value, language=language
            )
            valid_word.save()

        valid_word.update(add_to_set__translations=[translation])

    except Exception as ue_err:
        logger.error(str(ue_err))

    result = True
    return result


def remove(value, language):
    """Delete Word for App

    It creates a valid Word for the app. If the word exists,
    it will add the new translation to the word's translations. If it doens't
    it will create a new Word with the translation provided
    """
    if not check_spelling(value, language):
        raise ParameterExpected("Misspelled word provided!")

    result = False
    try:
        value = validate_string(value, "[^a-z]")
        valid_word = Word.objects(value=value, language=language).first()
        #word already exist so let's add a new translation
        if valid_word:
            valid_word.delete()
            result = True

    except Exception as ue_err:
        logger.error(str(ue_err))

    return result
