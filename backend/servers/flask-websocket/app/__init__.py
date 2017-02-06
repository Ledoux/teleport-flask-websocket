from flask import Flask,render_template
from flask_socketio import SocketIO,send,emit
import json
import os
import sys

APP_DIR = '/'.join(__file__.split('/')[:-1])
LIB_DIR = os.path.join(APP_DIR, 'lib')
sys.path.append(LIB_DIR)
from config import config_with_app
from routes import routes_with_app
from websockets import websockets_with_app_and_socketio

app = Flask(__name__)
app.config['APP_DIR'] = APP_DIR
socketio = SocketIO(app)

config_with_app(app)
routes_with_app(app)
websockets_with_app_and_socketio(app, socketio)

if __name__ == '__main__':
    app.run()
