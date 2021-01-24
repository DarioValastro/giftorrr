from flask_wtf import FlaskForm  # FORM
from wtforms import RadioField, SubmitField  # FIELD USED
from wtforms.validators import DataRequired

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





##############################
