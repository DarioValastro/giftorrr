import random


class Game:
    def __init__(self, questions, gifts):
        self.questions = questions
        self.giftsScore = {}  # to memorize score
        self.gifts = gifts
        self.giftNames = {}
        self.finalRank = []
        self.finalRankSecond = []

    def getQuestions(self):
        return self.questions

    def refreshGame(self):
        for g in self.gifts:
            self.giftsScore[g.getIdGift()] = 0

    def initializeGiftsScore(self):
        for g in self.gifts:
            self.giftsScore[g.getIdGift()] = 0
            self.giftNames[g.idGift] = g

    def addPoint(self, score):
        for g in self.gifts:
            for s in score:
                if s.getIdGift() == g.getIdGift():
                    if s.getValue() == -1:  # quando la risposta è -1 elimina automaticamente il regalo!
                        self.giftsScore.pop(g.idGift)  # check if OK
                        self.gifts.remove(g)
                        if g.getIdGift() == 15:
                            print('quiiiiii', g.getName())
                    else:
                        self.giftsScore[g.idGift] = self.giftsScore[g.idGift] + s.getValue()

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
                print(g.idGift, g.name, g.getPriceLL(), g.getPriceUL())
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

        # for g in self.gifts:
        #    print(g.idGift, g.name)

    def rank(self):
        self.giftsScore = dict(sorted(self.giftsScore.items(), key=lambda x: x[1], reverse=True))  # rank dictionary
        self.finalRank = []
        self.finalRankSecond = []
        print('DEBUG DA QUI:')
        print(self.giftsScore)
        first_step = True
        second_step=True
        first_point = 0
        second_position = 0
        third_position = 0
        print('first final rank', self.finalRank)
        for g in self.giftsScore:
            if first_step:
                first_step = False
                first_point = self.giftsScore[g]
                if first_point == self.giftsScore[g]:
                    self.finalRank.append(g)
            elif first_point == self.giftsScore[g]:
                self.finalRank.append(g)
            elif second_step:
                second_step=False
                second_point=self.giftsScore[g]
                if second_point == self.giftsScore[g]:
                    self.finalRankSecond.append(g)
            elif second_point == self.giftsScore[g]:
                self.finalRankSecond.append(g)
        print('final rank', self.finalRank)
        print('second final rank',self.finalRankSecond)
        id_first_gift = random.choice(self.finalRank)
        print('idregalo', id_first_gift)
        first_position = self.giftNames[id_first_gift]
        print('regalo', first_position.getName())
        self.finalRank.remove(id_first_gift)
        print('tolto?', self.finalRank)
        print('lunghezza', len(self.finalRank))
        if len(self.finalRank) == 1:
            id_second_gift = random.choice(self.finalRankSecond)
            print('idgift random', id_second_gift)
            second_position = self.giftNames[id_second_gift]
            print('regalo', second_position.getName())
            self.finalRankSecond.remove(id_second_gift)

            id_third_gift = random.choice(self.finalRankSecond)
            third_position = self.giftNames[id_third_gift]
            self.finalRankSecond.remove(id_third_gift)

            final_res = [first_position, second_position, third_position]
            return final_res
        else:
            id_second_gift = random.choice(self.finalRank)
            print('idgift random', id_second_gift)
            second_position = self.giftNames[id_second_gift]
            print('regalo', second_position.getName())
            self.finalRank.remove(id_second_gift)

            id_third_gift = random.choice(self.finalRank)
            third_position = self.giftNames[id_third_gift]
            self.finalRank.remove(id_third_gift)

        final_res = [first_position, second_position, third_position]

        perPrint = [first_position.getName(), second_position.getName(), third_position.getName()]
        print(perPrint)
        return final_res

    # TODO
    def addPointSustainable(self, idAnswer, score):
        pass
