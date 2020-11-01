class Answer:
    def __init__(self,idAnswer,idQuestion, textAnswer):
        self.idAnswer=idAnswer
        self.idQuestion=idQuestion
        self.textAnswer=textAnswer

    def getTextAnswer(self):
        return self.textAnswer

    def getIdAnswer(self):
        return self.idAnswer

    def getIdQuestion(self):
        return self.idQuestion




