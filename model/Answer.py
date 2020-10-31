class Answer:
    def __init__(self,idAnswer,idQuestion, textAnswer):
        self.idAnswer=idAnswer
        self.idQuestion=idQuestion
        self.textAnswer=textAnswer

    def getText(self):
        return self.textAnswer

    def getIDanswer(self):
        return self.idAnswer

    def getIDquestion(self):
        return self.idQuestion

    def setText(self, text):
        self.textAnswer = text
        return self.textAnswer

    def setIDanswer(self, id_a):
        self.idAnswer = id_a
        return self.idAnswer

    def setIDquestion(self, id_q):
        self.idQuestion = id_q
        return self.idQuestion
