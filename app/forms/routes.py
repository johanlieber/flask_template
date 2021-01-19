from flask import Blueprint

form_app = Blueprint('forms', __name__)

@form_app.route('/forms', methods=['GET', 'POST'])
def forms():
    return 'Form route'
