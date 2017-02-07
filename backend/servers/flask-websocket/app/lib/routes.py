from flask import render_template
import json

def routes_with_app(app):
    INDEX_HTML_NAME = '_index.html' if app.config['TYPE'] == 'localhost' else '_index_prod.html'

    context = {
        "SITE_NAME": app.config["SITE_NAME"],
        "TELEPORT_WELCOME": app.config["TELEPORT_WELCOME"],
        "TELEPORT_WELCOME_STRING": json.dumps(app.config["TELEPORT_WELCOME"]),
        "URL": app.config["URL"]
    }

    @app.route('/')
    def get_home():
    	return render_template(INDEX_HTML_NAME, **context)

    @app.route('/ping')
    def get_ping():
        return 'ping'

    # serve index for all paths, so a client side router can take over
    @app.route('/<path:path>')
    def get_home_redirect(path):
    	return get_home()
