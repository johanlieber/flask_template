from flask import render_template
from app import app

@app.errorhandler(404)
def no_page_there(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def no_page_there(e):
    return render_template('500.html'), 500

app.secret_key = ''

if __name__ == '__main__':
    app.run(debug=True)
