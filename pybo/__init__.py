from flask import Flask
from flask_migrate import Migrate #ORM 적용
from flask_sqlalchemy import SQLAlchemy #ORM 적용

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app

    #app.config.from_object(config)

    #@app.route('/')
    #def hello_pybo():
    #   return 'Hello, Pybo!"
    #return app

    #ORM
    #db.init_app(app)
    #migrate.init_app(app, db)
    #from . import models



# 데이터 베이스 초기화를 위해 flask db init 명령 실행 ㄱ
# flask db migrate

'''
app = Flask(__name__)은 플라스크 애플리케이션을 생성하는 코드다. 이 코드에서 __name__이라는 변수에는 모듈명이 담긴다. 
즉, 이 파일이 실행되면 pybo.py라는 모듈이 실행되는 것이므로 __name__ 변수에는 "pybo" 라는 문자열이 담긴다. 
@app.route는 특정 URL에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터다.

데코레이터(decorator)란 기존 함수를 변경하지 않고 추가 기능을 덧붙일 수 있도록 해주는 함수를 의미한다. 
좀 더 자세한 내용을 알고 싶다면 wikidocs.net/83687 을 참고하자.
'''
