from flask import Blueprint, render_template

views_app = Blueprint('views', __name__)

@views_app.route('/', methods=['GET', 'POST'])
def index():
    return 'Views route'
