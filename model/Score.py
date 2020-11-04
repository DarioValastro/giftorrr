class Scoree:

    def __init__(self, idGift, idAnswer, idQuestion, value):
        self.idGift = idGift
        self.idAnswer = idAnswer
        self.idQuestion = idQuestion
        self.value = value

    def getIdGift(self):
        return self.idGift

    def getValue(self):
        return self.value
