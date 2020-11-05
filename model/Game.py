class Game:
    def __init__(self, questions, gifts):
        self.questions = questions
        self.giftsScore = {}  # to memorize score
        self.gifts = gifts

    def getQuestions(self):
        return self.questions

    def initializeGiftsScore(self):
        for g in self.gifts:
            self.giftsScore[g.getIdGift()] = 0


    def addPoint(self, score):
        for g in self.gifts:
            for s in score:
                if s.getIdGift() == g.getIdGift():
                    #print("the value of gift " + str(s.getIdGift()) + " is " + str(s.getValue()))
                    self.giftsScore[g.idGift] = s.getValue()
        print(self.giftsScore)
