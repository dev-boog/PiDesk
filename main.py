from flask import Flask, render_template
from routes.system_routes import system_routes  

app = Flask(__name__)

# System Blueprint Registration
app.register_blueprint(system_routes)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5420, debug=True)
