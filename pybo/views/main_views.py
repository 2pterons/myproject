from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('question_list'))

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo! this is test!'

@bp.route('/main')
def main():
    return render_template('/index.html')

