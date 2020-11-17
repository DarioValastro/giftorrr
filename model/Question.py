class Question:
    def __init__(self, idQuestion, textQuestion,textQuestionIta):
        self.idQuestion = idQuestion
        self.textQuestion = textQuestion
        self.textQuestionIta = textQuestionIta

    def getTextQuestion(self):
        return self.textQuestion

    def getTextQuestionIta(self):
        return self.textQuestionIta

    def getIdQuestion(self):
        return self.idQuestion
