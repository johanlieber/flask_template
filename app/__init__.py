from flask import Flask, Blueprint

from app.config import settings

from app.forms.routes import form_app
from app.views.routes import views_app

app = Flask(__name__)

app.register_blueprint(forms.routes.form_app)
app.register_blueprint(views.routes.views_app)
