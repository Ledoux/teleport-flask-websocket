from flask_socketio import emit

def websockets_with_app_and_socketio(app, socketio):
    @socketio.on('test_ping')
    def test_ping(*args):
        emit('test_pong',*args,broadcast=True)
