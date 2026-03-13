
import logging
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session


db = SQLAlchemy()
login = LoginManager()
sess = Session()

app = Flask(__name__)
app.config.from_object(Config)


log_path = os.path.join('/tmp', 'app.log')

if not app.logger.handlers:

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(message)s'
    )

    # Stream handler (needed for Azure Log Stream)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    # File handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    app.logger.addHandler(stream_handler)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)


app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = '/tmp/flask_session'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True


db.init_app(app)
login.init_app(app)
sess.init_app(app)

login.login_view = 'login'


import FlaskWebProject.views

