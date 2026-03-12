import logging
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# --- FIXED LOGGING SECTION ---
# On Azure Linux, we log to /tmp to avoid permission errors in the root
log_path = os.path.join('/tmp', 'app.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# StreamHandler is essential for Azure "Log Stream" to work
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

app.logger.addHandler(stream_handler)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
# ------------------------------

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Circular import is fine at the bottom in Flask
import FlaskWebProject.views