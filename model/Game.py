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
                    # print("the value of gift " + str(s.getIdGift()) + " is " + str(s.getValue()))
                    if s.getValue() == -1: # quando la risposta elimina automaticamente il regalo!
                        self.giftsScore.pop(g.idGift) # check if OK
                        self.gifts.remove(g)
                    else:
                        self.giftsScore[g.idGift] = s.getValue()
        print(self.giftsScore)
        for g in self.gifts:
            print(g.idGift,g.name,g.getPriceLL(),g.getPriceUL())

    def deleteDueToPrice(self, idAnswer):
        tempGifts = []
        tempGiftsScore = {}
        if int(idAnswer) == 10:  # under 10€
            print(len(self.gifts))
            for g in self.gifts:
                print(g.idGift,g.name)
                if g.getPriceLL() <= 10 and g.getPriceUL()<=15:
                    tempGifts.append(g)
                    tempGiftsScore[g.idGift]=self.giftsScore[g.idGift]
            self.gifts=tempGifts
            self.giftsScore=tempGiftsScore
        # DA QUIIIIIIIIIIIIIIIIII
        elif idAnswer == 11:  # 10-20€
            for g in self.gifts:
                if g.getPriceLL() > 25 or g.getPriceUL() < 10:
                    del self.giftsScore[g.idGift]
                    self.gifts.remove(g)
        elif idAnswer == 12:  # 30-50€
            for g in self.gifts:
                if g.getPriceLL() > 50 or g.getPriceUL() < 25:
                    del self.giftsScore[g.idGift]
                    self.gifts.remove(g)
        elif idAnswer == 13:  # 50-100€
            for g in self.gifts:
                if g.getPriceLL() > 100 or g.getPriceUL() < 50:
                    del self.giftsScore[g.idGift]
                    self.gifts.remove(g)
        elif idAnswer == 14:  # 100-200€
            for g in self.gifts:
                if g.getPriceLL() > 200 or g.getPriceUL() < 100:
                    del self.giftsScore[g.idGift]
                    self.gifts.remove(g)
        elif idAnswer == 15:  # over 200€
            for g in self.gifts:
                if g.getPriceUL() < 200:
                    del self.giftsScore[g.idGift]
                    self.gifts.remove(g)

        print(self.giftsScore)
        for g in self.gifts:
            print(g.idGift,g.name)

