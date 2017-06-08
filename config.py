import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get("SECRET_KEY") or 'hard to guess string'
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True

  @staticmethod
  def init_app(app):
    pass

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
    'sqlite:///' + os.path.join(base_dir, 'data_dev.sqlite')

class TestConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
    'sqlite:///' + os.path.join(base_dir, 'data_test.sqlite')

class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
    'sqlite:///' + os.path.join(base_dir, 'data.sqlite')

config = {
  'deveopment': DevelopmentConfig,
  'testing': TestConfig,
  'production': ProductionConfig,

  'default': DevelopmentConfig
}
