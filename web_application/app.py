from flask import Flask, render_template
from web_application.routes.home_route import home_routes
from web_application.routes.settings_route import settings_routes
from web_application.routes.system_route import system_routes

app = Flask(__name__)

app.register_blueprint(home_routes)
app.register_blueprint(settings_routes)
app.register_blueprint(system_routes)

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5420, debug=True)
