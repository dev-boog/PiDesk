from flask import Flask, render_template
from web_application.routes.clock_route import clock_routes

app = Flask(__name__)

app.register_blueprint(clock_routes)

@app.route('/')
def index():
    return render_template('clock.html')

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5420, debug=True)
