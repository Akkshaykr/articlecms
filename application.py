import os
from FlaskWebProject import app

if __name__ == '__main__':
    # Azure will provide the PORT environment variable
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8000'))
    except ValueError:
        PORT = 8000
    
    app.run(HOST, PORT)