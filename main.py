from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    password = request.headers.get('pass')
    if password == 'xiaomilepsze':
        return 'done'
    return 'failure'


app.run()