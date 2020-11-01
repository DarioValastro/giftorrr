import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_wtf import FlaskForm  # FORM
from wtforms import RadioField, SubmitField  # FIELD USED
from wtforms.validators import DataRequired

# CONFIG APP
from model import Question

app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.debug = True
#######################


# DB
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9RLxFv1t3IVbRoJL@localhost/giftor'  # set the path for the database, ho installato dal terminal pymysql per farlo funzionare
app.config[
    'SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # set to True to enable automatic commits of database changes at the end of each request.
app.config[
    'SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # per evitare l'errore esplicitato in questo link: https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
db = SQLAlchemy(app)


class Questions(db.Model):
    # __tablename__ = "questions"
    idQuestion = db.Column('idQuestion', db.Integer, primary_key=True)
    textQuestion = db.Column(db.String)

    def __init__(self, textQuestion):
        self.textQuestion = textQuestion

    def __repr__(self):
        return '<Question %r>' % self.textQuestion


# FORMS
class AnswerForm(FlaskForm):
    answer = gender = RadioField('Gender', choices=['Male', 'Female', 'Neutrer'],
                                 validators=[DataRequired()])  # choiches from db
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


'''
@app.route('/test/')
def test():
    try:
        questions = Questions.query.filter_by().order_by(Questions.idQuestion).all()
        return render_template('test.html',)
       
        q_text = '<ul>'
        for q in questions:
            q_text += '<li>' + str(q.idQuestion) + ', ' + q.textQuestion + '</li>'
        q_text += '</ul>'
        return q_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
        '''
    # return render_template('test.html')

@app.route('/test')
def test():
    questions = Questions.query.distinct()
    counterQuestion=0
    res=[]
    for q in questions:
        res.append(q.textQuestion)
    return render_template('test.html', questions=res,counterQuestion=counterQuestion)



if __name__ == '__main__':
    app.run()
