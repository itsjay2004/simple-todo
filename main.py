from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)

# # This is because jinja's and vue's delimiter is clasing "{{ }}" 
# # So changed the jinja's delimiter from "{{ 'variable' }}" to "[[ 'variable' ]]" 
# app.jinja_env.variable_start_string = '[['
# app.jinja_env.variable_end_string = ']]'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ToDo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/')
def index():
    return render_template('index.html')




app.run(debug=True, host="0.0.0.0")