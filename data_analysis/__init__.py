from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)

app.secret_key = '1bd8e6f5070f0bf8c4710ab08646a51b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db?check_same_thread=False'
db = SQLAlchemy(app)
manager = Manager(app)
UPLOAD_FOLDER = 'data_analysis/files'
ALLOWED_EXTENSIONS = {'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@manager.command
def migrate():
    pass


from data_analysis import routes
