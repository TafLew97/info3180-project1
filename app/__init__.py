from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gnvlzvqvhlzvht:e4126efc560a854c1c2932b248ee8e9f3a3593a955dde934a4d4c51a6196e895@ec2-23-23-195-205.compute-1.amazonaws.com:5432/dckgdt54s9cbgm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning



app.config['ALLOWED_UPLOADS'] = set(['jpg','png','jpeg'])
db = SQLAlchemy(app)
app.config.from_object(__name__)

from app import views