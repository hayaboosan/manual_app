from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os


from config import DATABASE_URI
from config import engine


db = SQLAlchemy()
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
    return render_template('./index.html')
