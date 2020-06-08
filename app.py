# External imports
from flask import Flask

# Builtin imports
import json

app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps({"status": "success"})


if __name__ == '__main__':
    app.run()
