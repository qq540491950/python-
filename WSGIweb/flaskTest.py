from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hello,world"


@app.route("/")
def index():
    return "这是首页！"


if __name__ == '__main__':
    app.run()
