'''from app import db

class Question(db.Model):
    idQuestion = db.Column(db.Integer, db.ForeignKey('roles.id'))
    textQuestion = db.Column(db.TEXT)


    def __init__(self,idQuestion, textQuestion):
        self.idQuestion=idQuestion
        self.textQuestion=textQuestion

    def getText(self):
        return self.textQuestion

    def getIDquestion(self):
        return self.idQuestion

'''