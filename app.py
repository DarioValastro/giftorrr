import os

import mysql.connector

from flask import Flask, render_template
from flask_wtf import FlaskForm  # FORM
from wtforms import RadioField, SubmitField  # FIELD USED
from wtforms.validators import DataRequired


# CONFIG APP
app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.debug = True
#######################

"""
Non so i cosa inserire in app.config['SQLALCHEMY_DATABASE_URI']

#DB
#app.config['SQLALCHEMY_DATABASE_URI'] =\'mysql://localhost:admin@127.0.0.1/db' + os.path.join(basedir, 'data.sqlite') # set the path for the database
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True # set to True to enable automatic commits of database changes at the end of each request.
#######################
"""

#prova a vedere se cosi lo collega

mydb = mysql.connector.connect(
    host= "127.0.0.1",
    user = "root",
    password = "IS_project", #non so che password hai messo i dati qua sono riferiti al mio DB
    database= "Choose_gift", #è il nome del DB
)

my_cursor = mydb.cursor()




# FORMS
class AnswerForm(FlaskForm):
    answer = gender = RadioField('Gender', choices=['Male', 'Female', 'Neutrer'], validators=[DataRequired()]) # choiches from db
    submit = SubmitField('Submit')
#######################


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/contactUs/')
def contact_Us():
    return render_template('contactUs.html')


@app.route('/aboutUs/')
def about_Us():
    return render_template('aboutUs.html')


@app.route('/test/')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
