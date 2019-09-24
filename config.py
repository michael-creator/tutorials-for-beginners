import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michael:joker@localhost/pen'
#    @staticmethod
    def init_app(app):
       pass




class ProdConfig(Config):
#    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
# class TestConfig(Config):
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michael:joker@localhost/one_test'
class DevConfig(Config):
  
   DEBUG = True
config_options = {
   'development' : DevConfig,
   'production' : ProdConfig,
   'test':TestConfig
}

