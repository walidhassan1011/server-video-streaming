from flask import Flask

app = Flask(__name__,static_folder='static')
app.config['UPLOAD_FOLDER'] = 'static'
from application import routes