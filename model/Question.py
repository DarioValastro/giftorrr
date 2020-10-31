class Question:
    def __init__(self,idQuestion, textQuestion):
        self.idQuestion=idQuestion
        self.textQuestion=textQuestion

    def getText(self):
        return self.textQuestion

    def getIDquestion(self):
        return self.idQuestion

    def setText(self, text):
        self.textQuestion = text
        return self.textQuestion

    def setIDquestion(self, id):
        self.idQuestion = id
        return self.idQuestion

