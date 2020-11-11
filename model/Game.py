class Game:
    def __init__(self, questions, gifts):
        self.questions = questions
        self.giftsScore = {}  # to memorize score
        self.gifts = gifts
        self.giftNames = {}

    def getQuestions(self):
        return self.questions

    def initializeGiftsScore(self):
        for g in self.gifts:
            self.giftsScore[g.getIdGift()] = 0
            #print(g.idGift,str(g.name))
            self.giftNames[g.idGift] = str(g.name)

    def addPoint(self, score):
        for g in self.gifts:
            for s in score:
                if s.getIdGift() == g.getIdGift():
                    if s.getValue() == -1:  # quando la risposta è -1 elimina automaticamente il regalo!
                        self.giftsScore.pop(g.idGift)  # check if OK
                        self.gifts.remove(g)
                    else:
                        self.giftsScore[g.idGift] = s.getValue()

    def deleteDueToPrice(self, idAnswer):
        tempGifts = []
        tempGiftsScore = {}
        if int(idAnswer) == 10:  # under 10€
            for g in self.gifts:
                if g.getPriceLL() <= 10 and g.getPriceUL() <= 15:
                    tempGifts.append(g)
                    tempGiftsScore[g.idGift] = self.giftsScore[g.idGift]
            self.gifts = tempGifts
            self.giftsScore = tempGiftsScore
        elif int(idAnswer) == 11:  # 10-25€
            for g in self.gifts:
                print(g.idGift,g.name,g.getPriceLL(),g.getPriceUL())
                if g.getPriceLL() <= 25 and g.getPriceUL() > 10:
                    tempGifts.append(g)
                    tempGiftsScore[g.idGift] = self.giftsScore[g.idGift]
                    print('add')
                else:
                    print('no add')
            self.gifts = tempGifts
            self.giftsScore = tempGiftsScore
        elif int(idAnswer) == 12:  # 25-50€
            for g in self.gifts:
                if g.getPriceLL() <= 50 and g.getPriceUL() > 30:
                    tempGifts.append(g)
                    tempGiftsScore[g.idGift] = self.giftsScore[g.idGift]
            self.gifts = tempGifts
            self.giftsScore = tempGiftsScore
        elif int(idAnswer) == 13:  # 50-100€
            for g in self.gifts:
                if g.getPriceLL() <= 100 and g.getPriceUL() > 50:
                    tempGifts.append(g)
                    tempGiftsScore[g.idGift] = self.giftsScore[g.idGift]
            self.gifts = tempGifts
            self.giftsScore = tempGiftsScore
        elif int(idAnswer) == 14:  # 100-200€
            for g in self.gifts:
                if g.getPriceLL() <= 200 and g.getPriceUL() > 100:
                    tempGifts.append(g)
                    tempGiftsScore[g.idGift] = self.giftsScore[g.idGift]
            self.gifts = tempGifts
            self.giftsScore = tempGiftsScore
        elif int(idAnswer) == 15:  # over 200€
            for g in self.gifts:
                if g.getPriceLL() >= 100 and g.getPriceUL() >= 200:
                    tempGifts.append(g)
                    tempGiftsScore[g.idGift] = self.giftsScore[g.idGift]
            self.gifts = tempGifts
            self.giftsScore = tempGiftsScore

        #for g in self.gifts:
        #    print(g.idGift, g.name)

    def rank(self):
        self.giftsScore = dict(sorted(self.giftsScore.items(), key=lambda x: x[1],reverse=True)) # rank dictionary
        return self.giftsScore

    def addPointSustainable(self, idAnswer, score):
        pass

    def firstPosition(self):
        res = self.giftNames.get(list(self.giftsScore.keys())[0])
        return res

    def secondPosition(self):
        res = self.giftNames.get(list(self.giftsScore.keys())[1])
        return res

    def thirdPosition(self):
        res = self.giftNames.get(list(self.giftsScore.keys())[2])
        return res