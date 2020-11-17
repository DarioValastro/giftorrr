class Gift:
    def __init__(self, idGift, name, sustainability, url, pic, priceUL, priceLL, nameIta):
        self.idGift = idGift
        self.name = name
        self.sustainability = sustainability
        self.url = url  # TODO se più URL
        self.pic = pic
        self.priceUL = priceUL
        self.priceLL = priceLL
        self.nameIta = nameIta

    def getIdGift(self):
        return self.idGift

    def getName(self):
        return self.name

    def getNameIta(self):
        return self.nameIta

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

    def toString(self):
        return "Il regalo con id: " + str(self.idGift) + " e nome: " + self.name


