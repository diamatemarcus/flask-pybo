from flask import Flask
from flask_migrate import Migrate
from flask_simplemde import SimpleMDE
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
from sqlalchemy import MetaData

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])

    app.config['SIMPLEMDE_JS_IIFE'] = True
    app.config['SIMPLEMDE_USE_CDN'] = True

    SimpleMDE(app)

    # ORM
    db.init_app(app)
    # 제약 조건이름은 MetaData클래스의 사용 규칙을 정의
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models

    #print(f"__name__:{__name__}")

    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    #app.register_blueprint(chart_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime


    return app