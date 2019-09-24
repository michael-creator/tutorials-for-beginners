import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = 'asdfghjk98765'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michael:joker@localhost/post'
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    



class ProdConfig(Config):

    pass 
    

class DevConfig(Config):

    DEBUG = True

config_options = {
'development': DevConfig,
'production': ProdConfig,

}
