import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF = True
    SECRET_KEY = 'postgres'
    SQLALCHEMY_DATABASE_URI = os.environ['localhost:postgres:candle_bot_db']


class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class TestingConfig(Config):
    TESTING = True


