import os
import sys
from flask import Flask, render_template

# 1. Add the current directory to sys.path 
# This helps Vercel find the 'app' folder and 'scrapper.py'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app.scrapper import get_steampulse_data
except ImportError:
    # Fallback for different Vercel directory structures
    from scrapper import get_steampulse_data

app = Flask(__name__)

# 2. Fix the Template Path
# Point directly to where the HTML lives relative to this file
base_dir = os.path.dirname(os.path.abspath(__file__))
app.template_folder = os.path.join(base_dir, 'app', 'templates')

@app.route('/')
def index():
    games = get_steampulse_data()
    return render_template('index.html', games=games)

# 3. Vercel ignores the __main__ block, but we keep it for local testing
if __name__ == '__main__':
    app.run(debug=True)