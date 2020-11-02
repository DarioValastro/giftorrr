from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm  # FORM
from wtforms import RadioField, SubmitField, Field  # FIELD USED
from wtforms.validators import DataRequired

# CONFIG APP
app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.debug = True

# CONFIG DB
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9RLxFv1t3IVbRoJL@localhost/giftor'  # set the path for the database, ho installato dal terminal pymysql per farlo funzionare
app.config[
    'SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # set to True to enable automatic commits of database changes at the end of each request.
app.config[
    'SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # per evitare l'errore esplicitato in questo link: https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
db = SQLAlchemy(app)


# FORMS
class AnswerForm3(FlaskForm):
    submit = SubmitField('')
    answer = RadioField('Answer', choices=['1', '2', '3'],
                        validators=[DataRequired()])


class AnswerForm5(FlaskForm):
    submit = SubmitField('Submit')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5'],
                        validators=[DataRequired()])


class AnswerForm6(FlaskForm):
    submit = SubmitField('Submit')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5', '6'],
                        validators=[DataRequired()])


class AnswerForm10(FlaskForm):
    submit = SubmitField('Submit')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                        validators=[DataRequired()])
################################################################################################


# CLASS DB
class Questions(db.Model):
    __tablename__ = "questions"
    idQuestion = db.Column('idQuestion', db.Integer, primary_key=True)
    textQuestion = db.Column(db.String)

    def __init__(self, textQuestion):
        self.textQuestion = textQuestion

    def __repr__(self):
        return '<Question %r>' % self.textQuestion


class Answers(db.Model):
    __tablename__ = "answers"
    idAnswer = db.Column('idAnswer', db.Integer, primary_key=True)
    idQuestion = db.Column('idQuestion', db.Integer, primary_key=True)  # Non sono sicuro sul primary key
    textAnswer = db.Column('textAnswer', db.String)
###########################################################################################################


# FUNCTIONS
def getQuestionsFromDB():
    questions = Questions.query.distinct()
    resQuestions = []
    for q in questions:
        resQuestions.append(q.textQuestion)
    return resQuestions


def getAswersFromDB(count):
    answers = Answers.query.filter(Answers.idQuestion == count + 1)
    resAnswers = []
    for a in answers:
        resAnswers.append(a.textAnswer)
    return resAnswers


def getFormBasedOnLength(len):
    if len == 3:
        return AnswerForm3(request.form)
    elif len == 5:
        return AnswerForm5(request.form)
    elif len == 6:
        return AnswerForm6(request.form)
    elif len == 10:
        return AnswerForm10(request.form)
##############################################################################

#ROUTE
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


# PRIMA ROUTE DOMANDE
@app.route('/test', methods=['GET', 'POST'])
def test():
    try:
        count = 0
        path = 'Start'
        # Questions
        questions = getQuestionsFromDB()

        # Answers
        answers = getAswersFromDB(count)

        # form
        form = getFormBasedOnLength(len(answers))

        return render_template('test.html', questions=questions, counterQuestion=count, answers=answers,
                               form=form, path=path)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


# ALTRE ROUTE DOMANDE
@app.route('/testt/<idQuestion>/<path>', methods=['GET', 'POST'])
def testt(idQuestion=None, path=None):
    try:
        count = int(idQuestion) + 1
        path = path + "Q" + str(count) + ":A" + str(path) + "-"

        # Questions
        questions = getQuestionsFromDB()

        # Answers
        answers = getAswersFromDB(count)

        # form
        form = getFormBasedOnLength(len(answers))

        return render_template('test.html', questions=questions, counterQuestion=count, answers=answers,
                               form=form, path=path)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run()
