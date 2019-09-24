import os

class Config:

    SECRET_KEY = 'asdfghjk98765'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michael:joker@localhost/post'
    
    



class ProdConfig(Config):

    pass 
    

class DevConfig(Config):

    DEBUG = True

config_options = {
'development': DevConfig,
'production': ProdConfig,

}