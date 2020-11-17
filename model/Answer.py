class Answer:
    def __init__(self, idAnswer, idQuestion, textAnswer, textAnswerIta):
        self.idAnswer = idAnswer
        self.idQuestion = idQuestion
        self.textAnswer = textAnswer
        self.textAnswerIta = textAnswerIta

    def getTextAnswer(self):
        return self.textAnswer

    def getTextAnswerIta(self):
        return self.textAnswerIta

    def getIdAnswer(self):
        return self.idAnswer

    def getIdQuestion(self):
        return self.idQuestion
