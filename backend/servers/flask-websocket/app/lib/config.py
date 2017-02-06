import json
import os

default = {
    'DATA': "localhost",
    'SITE_NAME': "",
    'TYPE': "localhost",
    'URL': "http://localhost:5000"
}

def config_with_app (app):

    app.config['CONFIG_DIR'] = os.path.join(app.config['APP_DIR'], '../config')
    teleport_dir = os.path.join(app.config['CONFIG_DIR'], 'teleport.json')
    if os.path.isfile(teleport_dir):
        app.config['teleport'] = json.load(open(teleport_dir, 'r'))
    else:
        app.config['teleport'] = {}

    for couples in default.items():
    	app.config[couples[0]] = os.environ.get(
    		couples[0],
    		couples[1]
    	)
