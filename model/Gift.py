class Gift:
    def __init__(self, idGift, name, sustainability, url, pic, priceUL, priceLL):
        self.idGift = idGift
        self.name = name
        self.sustainability = sustainability
        self.url = url
        self.pic = pic
        self.priceUL = priceUL
        self.priceLL = priceLL

    def getIDgift(self):
        return self.idGift

    def getName(self):
        return self.name

    def getSustainability(self):
        return self.sustainability

    def getUrl(self):
        return self.url

    def getPic(self):
        return self.pic

    def getPriceUL(self):
        return self.priceUL

    def getPriceLL(self):
        return self.priceLL

#serve solo se dalla pagine web vogliamo modificare il DB (Dando la possibilità di aggiungere un regalo)

    def setIDgift(self,id_gift):
        self.idGift = id_gift
        return self.name

    def setName(self,name):
        self.name = name
        return self.name

    def setSustainability(self, sustain):
        self.sustainability = sustain
        return self.sustainability

    def setUrl(self, url):
        self.url = url
        return self.url

    def setPic(self, pic):
        self.pic = pic
        return self.pic

    def setPriceUL(self, price_ul):
        self.priceUL = price_ul

    def setPriceLL(self, price_ll):
        self.priceLL = price_ll
        return self.priceLL