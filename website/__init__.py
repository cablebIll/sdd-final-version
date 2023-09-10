from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "EG Demon1"  # not important

    from .views import views # import the blueprint from website/views.py

    app.register_blueprint(views, url_prefix='/')

    return app
