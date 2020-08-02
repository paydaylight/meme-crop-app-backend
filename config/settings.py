class BaseConfig:
    TESTING = False
    DEBUG = False
    API_PREFIX = '/api'
    API_V1_PREFIX = '/api/v1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    ENV = FLASK_ENV
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/flask-app'


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-app'


class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True