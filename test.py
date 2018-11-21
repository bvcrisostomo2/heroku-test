from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
fro

app = Flask(__name__)


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def helloWorld():
    return "Hello World"



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
