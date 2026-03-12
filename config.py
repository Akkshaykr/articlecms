import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'akkshay'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'BLOB_KEY_HERE'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'akkshay.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'akkshay'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'akkshay'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'password@01'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://akkshay:password%4001@akkshay.database.windows.net:1433/akkshay?driver=ODBC+Driver+17+for+SQL+Server&Encrypt=yes&TrustServerCertificate=yes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'CLIENT_SECRET_HERE'
    AUTHORITY = "https://login.microsoftonline.com/f958e84a-92b8-439f-a62d-4f45996b6d07"
    
    CLIENT_ID = "2650d5c2-ddc3-4597-bb6b-0bdbf9ce04f9"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"