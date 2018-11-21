from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return "Hello World"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
