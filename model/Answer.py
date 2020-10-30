class Answer:
    def __init__(self,idAnswer,idQuestion, textAnswer):
        self.idAnswer=idAnswer
        self.idQuestion=idQuestion
        self.textAnswer=textAnswer

    def getText(self):
        return self.textAnswer
