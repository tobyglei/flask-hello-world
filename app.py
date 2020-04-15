from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '21云盒子 Hello Flask 样例'
