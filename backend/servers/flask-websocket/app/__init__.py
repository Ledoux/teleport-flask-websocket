#
# IMPORTS
#
import sys
from flask import Blueprint,Flask,flash,g,render_template
from flask_socketio import SocketIO,send,emit
import os
import hmac
import json
server_dir = '/'.join(__file__.split('/')[:-1])
sys.path.append(os.path.join(server_dir, 'lib'))
sys.path.append(os.path.join(server_dir, 'modules'))

#
# FLASK
#
app = Flask(__name__)

#
# SOCKETIO
#
socketio = SocketIO(app)

#
# ON (BE CAREFUL "ping" event name is not allowed)
#
@socketio.on('test_ping')
def test_ping(*args):
    emit('test_pong',*args,broadcast=True)

#
# CONFIG
#
default = {
    'DATA': "localhost",
    'SMTP_HOST': "localhost",
    'SITE_NAME': "",
    'TYPE': "localhost",
    'WEB': "on",
    'URL': "http://localhost:5000"
}
config = {}
for couples in default.items():
	app.config[couples[0]] = os.environ.get(
		couples[0],
		couples[1]
	)
app.config['HOST_DIR'] = "./" if app.config['TYPE'] != 'localhost' else os.path.join(os.getcwd().split('backend')[0], 'backend/')

#
# SECRET
#
config_dir = './config'
secret_dir = os.path.join(config_dir, 'secret.json')
with open(secret_dir, 'r') as file:
    app.config.update(json.load(file))

#
# DATABASES
#
app.config['databases_by_name'] = {}

#
# CLIENT SECRET
#
client_secret_name = app.config['TYPE'] + '_client_secret.json'
client_secret_path = os.path.join(config_dir, client_secret_name)
if os.path.isfile(client_secret_path):
    with open(client_secret_path,'r') as cl_se:
        app.config["GOOGLE_CLIENT_ID"] = json.load(cl_se)['web']['client_id']

#
# FLASK ENV
#
flask_env = {
    "SITE_NAME": app.config["SITE_NAME"],
    "URL": app.config["URL"],
    "WEB": app.config["WEB"]
}

#
# ROUTES
#
INDEX_HTML_NAME = '_index.html' if app.config['TYPE'] == 'localhost' else '_index_prod.html'

@app.route('/')
def get_home():
	return render_template(
        INDEX_HTML_NAME,
        **flask_env
    )

@app.route('/ping')
def get_ping():
    return 'ping'

# serve index for all paths, so a client side router can take over
@app.route('/<path:path>')
def get_home_redirect(path):
	return get_home()

#
# LOGIN
#
# if the module private is not inside the module folder,
# then the login manager of flask is not called to be set.
# By a certain non explained almost magical reason, this fix the property of
# the flask to render static files.
is_login = os.path.isfile('./app/modules/private.py')
if is_login:
    from flask.ext.login import LoginManager,current_user
    login_manager = LoginManager(app)
    login_manager.login_view = 'private.login_index'
    @app.before_request
    def add_user_before_request():
        g.user = current_user

#
# BLUEPRINTS
#
# then we can also go to specific modules inside this webserver
modules_path = os.path.join(server_dir, 'modules')
if os.path.isdir(modules_path):
    sys.path.append(modules_path)
    module_names = map(
        lambda fcouples:
        fcouples[0],
        filter(
            lambda couples:
            couples[-1]=='py' and couples[0] != "__init__",
            map(
                lambda file_name:
                file_name.split('.'),
                filter(
                    lambda dir_name:
                    dir_name[0] != ".",
                    os.listdir(modules_path)
                )
            )
        )
    )
else:
    module_names = []
# and also it specific libs
lib_path = os.path.join(server_dir, 'lib')
if os.path.isdir(lib_path):
    sys.path.append(lib_path)
    lib_names = map(
        lambda fcouples:
        fcouples[0],
        filter(
            lambda couples:
            couples[-1]=='py' and couples[0] != "__init__",
            map(
                lambda file_name:
                file_name.split('.'),
                filter(
                    lambda dir_name:
                    dir_name[0] != ".",
                    os.listdir(lib_path)
                )
            )
        )
    )
    for lib_name in lib_names:
        __import__(lib_name)
# once the modules and libs are imported we can now
# also plug the blueprints flask to the app
map(
    lambda module:
    app.register_blueprint(getattr(module,'blueprint')),
    filter(
        lambda module:
        hasattr(module,'blueprint'),
        map(
            lambda module_name:
            __import__(module_name),
            module_names
        )
    )
)

#
# TABLES
#
app.config['tables_by_name'] = {}
for database_name, database in app.config['databases_by_name'].items():
    for table in database['tables']:
        table['database_name'] = database_name
        app.config['tables_by_name'][table['name']] = table

#
# RUN
#
if __name__ == '__main__':
    app.run()
