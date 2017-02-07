import os
import sys
sys.path.append(os.path.join('/'.join(__file__.split('/')[:-1]), '../'))
from app import app,socketio

PORT = 5001
URL = os.environ.get('URL', 'http://localhost:' + str(PORT))
SERVER = '//'.join(URL.split('//')[1:])
if ':' in SERVER:
    PORT = int(SERVER.split(':')[-1])
elif 'PORT' in os.environ:
    PORT = int(os.environ['PORT'])

if __name__ == '__main__':
    socketio.run(
        app,
        host = '0.0.0.0',
        port = PORT,
        use_reloader = app.config['TYPE'] == 'localhost'
    )
