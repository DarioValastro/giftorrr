import urllib, smtplib, os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_wtf import FlaskForm  # FORM
from wtforms import RadioField, SubmitField  # FIELD USED
from wtforms.validators import DataRequired
from model.Answer import Answer
from model.Game import Game
from model.Gift import Gift
from model.Question import Question
from model.Score import Scoree
from flask_mail import Message, Mail

# CONFIG APP
app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.debug = True
mail = Mail(app)

# CONFIG DB
params = urllib.parse.quote_plus(
    'Driver={SQL Server};Server=tcp:giftor.database.windows.net,'
    '1433;Database=giftor;Uid=amministratore;Pwd=' + os.environ['Pass_db'] + ';Encrypt=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9RLxFv1t3IVbRoJL@localhost/giftor'  # set the path
# for the database, ho installato dal terminal pymysql per farlo funzionare
app.config[
    'SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False  # set to True to enable automatic commits of database changes at the end
# of each request.
app.config[
    'SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # per evitare l'errore esplicitato in questo link:
# https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
db = SQLAlchemy(app)  # create DB


# FORMS English
class AnswerForm3(FlaskForm):
    submit = SubmitField('CONTINUE')
    answer = RadioField('Answer', choices=['1', '2', '3'],
                        validators=[DataRequired()])


class AnswerForm5(FlaskForm):
    submit = SubmitField('CONTINUE')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5'],
                        validators=[DataRequired()])


class FormFeedback(FlaskForm):
    finish = SubmitField('Send feedback and discover a surprise')
    feedback = RadioField('Feedback', choices=['1', '2', '3', '4', '5'],
                          validators=[DataRequired()])


class AnswerForm6(FlaskForm):
    submit = SubmitField('CONTINUE')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5', '6'],
                        validators=[DataRequired()])


class AnswerForm9(FlaskForm):
    submit = SubmitField('CONTINUE')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                        validators=[DataRequired()])


class AnswerForm10(FlaskForm):
    submit = SubmitField('CONTINUE')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                        validators=[DataRequired()])


class AnswerForm11(FlaskForm):
    submit = SubmitField('CONTINUE')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
                        validators=[DataRequired()])


def getFormBasedOnLength(length):
    if length == 3:
        return AnswerForm3(request.form)
    elif length == 5:
        return AnswerForm5(request.form)
    elif length == 6:
        return AnswerForm6(request.form)
    elif length == 9:
        return AnswerForm9(request.form)
    elif length == 10:
        return AnswerForm10(request.form)
    elif length == 11:
        return AnswerForm11(request.form)


################################################################################################

# FORMS Ita
class AnswerFormIta3(FlaskForm):
    submit = SubmitField('CONTINUA')
    answer = RadioField('Answer', choices=['1', '2', '3'],
                        validators=[DataRequired()])


class AnswerFormIta5(FlaskForm):
    submit = SubmitField('CONTINUA')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5'],
                        validators=[DataRequired()])


class FormFeedbackIta(FlaskForm):
    finish = SubmitField('Invia la valutazione e scopri una sorpresa')
    feedback = RadioField('Feedback', choices=['1', '2', '3', '4', '5'],
                          validators=[DataRequired()])


class AnswerFormIta6(FlaskForm):
    submit = SubmitField('CONTINUA')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5', '6'],
                        validators=[DataRequired()])


class AnswerFormIta9(FlaskForm):
    submit = SubmitField('CONTINUA')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                        validators=[DataRequired()])


class AnswerFormIta10(FlaskForm):
    submit = SubmitField('CONTINUA')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                        validators=[DataRequired()])


class AnswerFormIta11(FlaskForm):
    submit = SubmitField('CONTINUA')
    answer = RadioField('Answer', choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
                        validators=[DataRequired()])


def getFormBasedOnLengthIta(length):
    if length == 3:
        return AnswerFormIta3(request.form)
    elif length == 5:
        return AnswerFormIta5(request.form)
    elif length == 6:
        return AnswerFormIta6(request.form)
    elif length == 9:
        return AnswerFormIta9(request.form)
    elif length == 10:
        return AnswerFormIta10(request.form)
    elif length == 11:
        return AnswerFormIta11(request.form)


##############################

# CLASS DB
class Questions(db.Model):
    idQuestion = db.Column('idQuestion', db.Integer, primary_key=True)
    textQuestion = db.Column('textQuestion', db.String)
    textQuestionIta = db.Column('textQuestionIta', db.String)


class Questionnaires(db.Model):
    idQuiz = db.Column('idQuiz', db.Integer, primary_key=True, autoincrement=False)
    pathQuiz = db.Column('pathQuiz', db.String)
    rankGifts = db.Column('rankGifts', db.String)
    feedback = db.Column('feedback', db.Integer)


class Answers(db.Model):
    idAnswer = db.Column('idAnswer', db.Integer, primary_key=True)
    idQuestion = db.Column('idQuestion', db.Integer, primary_key=True)
    textAnswer = db.Column('textAnswer', db.String)
    textAnswerIta = db.Column('textAnswerIta', db.String)


class Gifts(db.Model):
    idGift = db.Column('idGift', db.Integer, primary_key=True)
    textGift = db.Column('textGift', db.String)
    link = db.Column('link', db.String)
    pic = db.Column('pic', db.String)
    sustainable = db.Column('sustainable', db.Integer)
    priceUL = db.Column('priceUL', db.Integer)
    priceLL = db.Column('priceLL', db.Integer)
    textGiftIta = db.Column('textGiftIta', db.String)
    tech = db.Column('tech', db.Integer)


class Score(db.Model):
    idGift = db.Column('idGift', db.Integer, primary_key=True)
    idQuestion = db.Column('idQuestion', db.Integer, primary_key=True)
    idAnswer = db.Column('idAnswer', db.Integer, primary_key=True)
    point = db.Column('point', db.Integer)


###########################################################################################################


# FUNCTIONS

def getQuestionsFromDB():
    questions = Questions.query.distinct()
    resQuestions = []
    for q in questions:
        resQuestions.append(Question(idQuestion=q.idQuestion, textQuestion=q.textQuestion,
                                     textQuestionIta=q.textQuestionIta))
    return resQuestions


def finishQuestions(count):
    if count == 8:
        return True
    else:
        return False


def sendPathToDB(path, rank):
    countQuiz = Questionnaires.query.count()
    countQuiz = countQuiz + 1
    rankGifts = ''
    for r in rank:
        rankGifts = rankGifts + "--" + r.getName() + "[" + str(r.getIdGift()) + "]"
    # print("rank gifts is     ", rankGifts)
    quiz = Questionnaires(idQuiz=countQuiz, pathQuiz=path, rankGifts=rankGifts, feedback=0)
    db.session.add(quiz)
    db.session.commit()
    return countQuiz


def sendFeedbackToDB(feedback, lastId):
    feedbackInt = int(feedback)
    print('the feedback is  ', feedbackInt)
    print('the last id is ', lastId)
    quiz = Questionnaires.query.filter(Questionnaires.idQuiz == lastId)
    quiz[0].feedback = feedback
    db.session.commit()
    pass


def getAnswersFromDB(count):
    answers = Answers.query.filter(Answers.idQuestion == count + 1)
    resAnswers = []
    for a in answers:
        resAnswers.append(
            Answer(idAnswer=a.idAnswer, idQuestion=count + 1, textAnswer=a.textAnswer, textAnswerIta=a.textAnswerIta))
    return resAnswers


def getGiftsFromDB():
    gifts = Gifts.query.distinct()
    resGifts = []
    for g in gifts:
        resGifts.append(Gift(idGift=g.idGift, name=g.textGift, sustainability=g.sustainable, url=g.link, pic=g.pic,
                             priceUL=g.priceUL, priceLL=g.priceLL, nameIta=g.textGiftIta, tech=g.tech))
    return resGifts


def getPointsFromDB(idAnswer, idQuestion):
    score = Score.query.filter((Score.idAnswer == idAnswer) & (Score.idQuestion == idQuestion))
    resScore = []
    for s in score:
        # print(s.idGift,s.idAnswer,s.idQuestion,s.point)
        resScore.append(Scoree(idGift=s.idGift, idQuestion=s.idQuestion, idAnswer=s.idAnswer, value=s.point))
    return resScore


# CONFIG GAME
count = 0
path = 'Start'

# Questions
questions = getQuestionsFromDB()
gifts = getGiftsFromDB()

game = Game(questions, gifts)
game.initializeGiftsScore()


######


# ROUTE
@app.route('/')
def home():
    game.refreshGame()
    count = 0
    return render_template('home.html', language='eng')


@app.route('/contactUs/')
def contact_Us():
    game.refreshGame()
    count = 0
    return render_template('contactUs.html', language='eng')


@app.route('/send_message_eng', methods=["POST", "GET"])
def send_message_eng():
    smtplibObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtplibObj.ehlo()
    smtplibObj.starttls()
    smtplibObj.login("ISProject.GIFTOR2020@gmail.com", os.environ['Pass_gmail'])

    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        # print("here sub" +subject)
        msg = request.form['message']
        body = subject + "\n " + "Email: \n " + email + "\n" + "Text: \n" + msg

        smtplibObj.sendmail("ISProject.GIFTOR2020@gmail.com", "ISProject.GIFTOR2020@gmail.com", body)
        smtplibObj.quit()

        success = "Message sent"

        return render_template("email_success.html", success=success)
    elif request.method == "GET":
        return render_template("email_success.html")


@app.route('/aboutUs/')
def about_Us():
    game.refreshGame()
    count = 0
    return render_template('aboutUs.html', language='eng')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', language='eng')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', language='eng')


# ROUTE ita_page
@app.route('/ita')
def home_ita():
    game.refreshGame()
    count = 0
    return render_template('home_ita.html', language='ita')


@app.route('/contactUs_ita/')
def contact_Us_ita():
    game.refreshGame()
    count = 0
    return render_template('contactUs_ita.html', language='ita')


@app.route('/send_message', methods=["POST", "GET"])
def send_message():
    smtplibObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtplibObj.ehlo()
    smtplibObj.starttls()
    smtplibObj.login("ISProject.GIFTOR2020@gmail.com", os.environ['Pass_gmail'])

    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        # print("here sub" +subject)
        msg = request.form['message']
        body = subject + "\n " + "Email: \n " + email + "\n" + "Text: \n" + msg

        smtplibObj.sendmail("ISProject.GIFTOR2020@gmail.com", "ISProject.GIFTOR2020@gmail.com", body)
        smtplibObj.quit()

        success = "Messaggio spedito"

        return render_template("email_success_ita.html", success=success)
    elif request.method == "GET":
        return render_template("email_success_ita.html")


@app.route('/aboutUs_ita/')
def about_Us_ita():
    game.refreshGame()
    count = 0
    return render_template('aboutUs_ita.html', language='ita')


# PRIMA ROUTE DOMANDE
@app.route('/test', methods=['GET', 'POST'])
def test():
    try:
        # Answers
        answers = getAnswersFromDB(count)
        print(count)
        # form
        form = getFormBasedOnLength(len(answers))

        return render_template('test.html', questions=game.questions, counterQuestion=count, answers=answers,
                               form=form, path=path, language='eng')
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


# ALTRE ROUTE DOMANDE
@app.route('/testt/<idQuestion>/<path>', methods=['GET', 'POST'])
def testt(idQuestion=None, path=None):
    try:
        print('idQuestion', idQuestion)
        count = int(idQuestion) + 1
        print('count ', count)

        # Answers
        answers = getAnswersFromDB(count)  # risposte alla domanda attuale

        # form
        form = getFormBasedOnLength(len(answers))

        # add point to gifts
        idanswer = form.answer.data
        print('idanswer', idanswer)
        score = getPointsFromDB(idAnswer=idanswer, idQuestion=count)

        if count == 3:  # è la domanda sul prezzo
            game.deleteDueToPrice(idAnswer=idanswer)
        elif count == 5:  # è la domanda sulla Sostenibilità
            game.addPointSustainable(score=score)
        elif count == 7:
            game.addPointTech(score=score)
        else:
            game.addPoint(score=score)

        path = path + "Q" + str(count) + ":A" + str(idanswer) + "--"

        if finishQuestions(count):
            # print('idanswer', idanswer)
            print('il path è     ', path)
            rank = game.rank()
            lastId = sendPathToDB(path, rank)

            formFeedback = FormFeedback(request.form)
            return render_template('result.html', rank=rank, language='eng', formFeedback=formFeedback,
                                   feedback_done=False, finishQuestion=True, lastId=lastId)
        else:
            return render_template('test.html', questions=game.questions, counterQuestion=count, answers=answers,
                                   form=form, path=path, language='eng')
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@app.route('/result/<lastId>', methods=['GET', 'POST'])
def result(lastId):
    try:
        formFeedback = FormFeedback(request.form)
        # feedback = formFeedback.feedback.data
        # print("The feedback is:   ", str(feedback))
        feedback = request.form['feedback']
        print("The feedback is:   ", str(feedback))
        sendFeedbackToDB(feedback, lastId)
        return render_template('result.html', rank=game.getRank(), language='eng', formFeedback=formFeedback,
                               feedback_done=True)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@app.route('/test_ita', methods=['GET', 'POST'])
def test_ita():
    try:
        # Answers
        answers = getAnswersFromDB(count)

        # form
        form = getFormBasedOnLengthIta(len(answers))

        return render_template('test_ita.html', questions=game.questions, counterQuestion=count, answers=answers,
                               form=form, path=path, language='ita')
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


# ALTRE ROUTE DOMANDE
@app.route('/testt_ita/<idQuestion>/<path>', methods=['GET', 'POST'])
def testt_ita(idQuestion=None, path=None):
    try:
        count = int(idQuestion) + 1  # contatore idQuestion
        print('count', count)
        # Answers
        answers = getAnswersFromDB(count)  # risposte alla domanda attuale

        # form
        form = getFormBasedOnLengthIta(len(answers))

        # add point to gifts
        idanswer = form.answer.data
        print('idanswer', idanswer)
        score = getPointsFromDB(idAnswer=idanswer, idQuestion=count)
        if count == 3:  # è la domanda sul prezzo
            game.deleteDueToPrice(idAnswer=idanswer)
        elif count == 5:  # è la domanda sulla Sostenibilità
            game.addPointSustainable(score=score)
        elif count == 7:
            game.addPointTech(score=score)
        else:
            game.addPoint(score=score)

        path = path + "Q" + str(count) + ":A" + str(idanswer) + "--"

        if finishQuestions(count):
            # sendPathToDB(path, count, form.answer.data)
            print('il path è     ', path)
            rank = game.rank()
            lastId = sendPathToDB(path, rank)
            return render_template('result_ita.html', rank=rank, language='ita', lastId=lastId,
                                   formFeedback=FormFeedbackIta(request.form), feedback_done=False)
        else:
            return render_template('test_ita.html', questions=game.questions, counterQuestion=count, answers=answers,
                                   form=form, path=path, language='ita')
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@app.route('/resultIta/<lastId>', methods=['GET', 'POST'])
def resultIta(lastId):
    try:
        formFeedback = FormFeedbackIta(request.form)
        # feedback = formFeedback.feedback.data
        # print("The feedback is:   ", str(feedback))
        feedback = request.form['feedback']
        print("The feedback is:   ", str(feedback))
        sendFeedbackToDB(feedback, lastId)
        return render_template('result_ita.html', rank=game.getRank(), language='ita', formFeedback=formFeedback,
                               feedback_done=True)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run()
