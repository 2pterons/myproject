# 파이보 프로젝트를 설정하는 config.py 파일
'''
config.py 파일은 파이보 프로젝트의 환경을 설정한다. 파이보 프로젝트의 환경변수, 데이터베이스 등의 설정을 이 파일에 저장한다.
'''
import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

'''
명령어               설명
flask db migrate	모델을 새로 생성하거나 변경할 때 사용 (실행하면 작업파일이 생성된다.)
flask db upgrade	모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용 (위에서 생성된 작업파일을 실행하여 데이터베이스를 변경한다.)

[질문 모델 속성]
속성명	    설명
id	        질문 데이터의 고유 번호
subject	    질문 제목
content	    질문 내용
create_date	질문 작성일시

답변 모델은 다음과 같은 속성이 필요하다.

[답변 모델 속성]
속성명	    설명
id	        답변 데이터의 고유 번호
question_id	질문 데이터의 고유 번호(어떤 질문에 달린 답변인지 알아야 하므로 질문 데이터의 고유 번호가 필요하다)
content	    답변 내용
create_date	답변 작성일시
'''
