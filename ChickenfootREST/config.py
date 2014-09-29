class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    SERVER_NAME = 'localhost'
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,

    'default' : ProductionConfig
}