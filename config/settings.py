class BaseConfig():
    API_PREFIX = '/api'
    TESTING = False
    DEBUG = False
    API_V1_PREFIX = '/api/v1'


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-app'


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-flask'


class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True