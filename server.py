from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'I\'m Flask. Hello from Docker!'


if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=5000)