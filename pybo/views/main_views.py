from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('/index.html')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo! this is test!'

@bp.route('/main')
def main():
    return render_template('/index.html')


