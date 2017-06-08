from flask import render_template
from . import main
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@main.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
  user = User.query.filter_by(username=name).first()
  username = user.username if user is not None else None
  return render_template('user.html', name=username)
