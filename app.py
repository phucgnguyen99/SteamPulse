import os
from flask import Flask, render_template
from app.scrapper import get_steampulse_data 

# Initialize the Flask application
app = Flask(__name__, template_folder='templates')

# Vercel needs to see 'app' as the entry point
# We also need to help Flask find the templates if it's struggling
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app', 'templates')

# Define a route for the homepage
@app.route('/')
def index():
    # Fetch live data on page load
    games = get_steampulse_data()
    return render_template('index.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)