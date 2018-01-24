from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
io = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')
