from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Fastwater callback active", 200

