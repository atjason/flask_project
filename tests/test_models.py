
import pytest
from flask import current_app
from app import create_app, db
from app.models import User

class TestUser():

  @classmethod
  def setup_class(cls):
    cls.app = create_app('testing')
    cls.app_context = cls.app.app_context()
    cls.app_context.push()
    # db.create_all()
  
  @classmethod
  def teardown_class(cls):
    db.session.remove()
    # db.drop_all()
    cls.app_context.pop()

  def test_app_exists(self):
    assert current_app is not None

  def test_app_is_testing(self):
    assert current_app.config['TESTING'] is not None

  def test_db_user(self):
    user = User.query.filter_by(username='AAA').first()
    assert user is None

    user = User.query.filter_by(username='Jason').first()
    assert user is not None
