import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'C6Eb4ynUH6=+!Gj=dBDD9X284m+yqPbPvuQuKYJ-zeehP9&=AFX52eQQmA&YsKyZ'
    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGODB_NAME') or 'transaltions',
        'host': os.environ.get('MONGODB_URI') or 'mongodb://db_adminusr:xAMrne;^8DS<C~>2@ds045897.mlab.com:45897/transaltions?retryWrites=false&socketTimeoutMS=10000&connectTimeoutMS=10000'
    }
    ENVIRONMENT = os.environ.get('ENVIRONMENT') or "DEVELOPMENT"
