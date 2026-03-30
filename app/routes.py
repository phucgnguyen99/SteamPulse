from flask import render_template, current_app as app
# This pulls get_steampulse_data from your scrapper.py
from .scrapper import get_steampulse_data 

@app.route('/')
def index():
    games = get_steampulse_data()
    return render_template('index.html', games=games)