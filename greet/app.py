from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
        <h1>Homepage</h1>
        <p>This is the homepage</p>
        </body>
    </html>
    """
    return html


@app.route('/welcome')
def welcome():
    html = """
    <html>
        <body>
        <h1>Welcome</h1>
        <p>Welcome</p>
        </body>
    </html>
    """
    return html

@app.route('/welcome/home')
def welcome_home():
    html = """
    <html>
        <body>
        <h1>Welcome Home</h1>
        <p>Welcome Home</p>
        </body>
    </html>
    """
    return html

@app.route('/welcome/back')
def welcome_back():
    html = """
    <html>
        <body>
        <h1>Welcome Back</h1>
        <p>Welcome Back</p>
        </body>
    </html>
    """
    return html
