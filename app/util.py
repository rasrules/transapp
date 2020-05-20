"""App Utils

Declaration of App Util methods
"""
import re
from unidecode import unidecode
from spellchecker import SpellChecker
# pylint: disable=import-outside-toplevel, consider-using-ternary


# #####################CONSTANTS##############################




def valid_start_string(value="", pattern=""):
    """Verifies if the string matches the start pattern string"""
    if not value or not pattern:
        return False

    return not re.match(pattern, value) is None


def validate_string(value, valid_chars):
    """Clean characters
    We replace unicode chars with base characters and then
    we clean the coming string according to the allowed
    ( valid_chars)
    """
    if value:
        value = unidecode(value)
    return value and re.sub(valid_chars, '', value) or None


def check_spelling(word, language='en'):
    """Verifies Spelling
    the word's spelling is checked according to the language selected
    """
    spell = SpellChecker(language=language)

    if word == '':  # not sure, but need a way to kill the program...
        print("no word found")
        return False

    word = word.lower()
    return word in spell and True or False
