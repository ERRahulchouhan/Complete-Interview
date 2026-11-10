from flask import Flask, render_template
from flask import Blueprint

# Create the Flask app
app = Flask(__name__)

# Create a Blueprint named 'my_blueprint'
my_blueprint = Blueprint('my_blueprint', __name__, url_prefix='/blueprint')

# Define a route inside the Blueprint
@my_blueprint.route('/')
def index():
    return 'Welcome to the Blueprint!'

# Register the Blueprint with the app
app.register_blueprint(my_blueprint)

# Define a route for the main app
@app.route('/')
def main_index():
    return 'Welcome to the main app!'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
