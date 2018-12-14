'''Configuration files for the API'''

class Config(object):
    '''Parent configuration class'''
    DEBUG = False
    SECRET_KEY = 'tryandguess'
    ENV = 'development'


class DevelopmentConfig(Config):
    '''configurations for development environment'''
    DEBUG = True


class StagingConfig(Config):
    '''configurations for staging environment'''
    DEBUG = True


class ProductionConfig(Config):
    '''configurations for production environment'''
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}