from flask import Flask, render_template, request

# TODO 1: Import the main limiter class and the utility function
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# EDUCATIONAL NOTE: 
# We are storing the password in plain text here ONLY to keep this lab simple.
# In the real world, you would NEVER do this. You would use bcrypt!
users_db = {"alice": "password123"}

# TODO 2: Initialize the rate limiter.
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memory://",
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
# TODO 3: Apply the appropriate rate-limiting decorator
@limiter.limit("5 per minute")
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check credentials
        if username in users_db and users_db[username] == password:
            return render_template('dashboard.html', username=username), 200
        else:
            error = "Invalid username or password."
            return render_template('login.html', error=error), 401

    return render_template('login.html', error=error)

# TODO 4: Create a global error handler for HTTP 429 (Too Many Requests).
@app.errorhandler(429)
def ratelimit_handler(e):
    return render_template('login.html', error="Rate limit exceeded. Try again later."), 429

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)