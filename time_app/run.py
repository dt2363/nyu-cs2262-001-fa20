from datetime import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def return_time():
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
