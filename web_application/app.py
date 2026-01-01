from flask import Flask, render_template
from web_application.routes.clock_route import clock_routes
from web_application.routes.settings_route import settings_routes
from web_application.routes.system_route import system_routes

app = Flask(__name__)

app.register_blueprint(clock_routes)
app.register_blueprint(settings_routes)
app.register_blueprint(system_routes)

@app.route('/')
def index():
    return render_template('clock.html')

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5420, debug=True)
