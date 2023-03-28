class Account:
    def __init__(self,Name,Tel,Summe):
        self.Name = Name
        self.Tel = Tel
        self.summe = Summe
     def accountInfo(self):
        print("Name : ",self.Name)
        print("Tel : ",self.Tel)
        print("Summe : ",self.summe)
    def geldAusgeben(self, wert):
        if (self.summe - wert < 0):
            print("Ihre Konto ist nicht reicht...")
        else:
            self.summe -= wert
            print("Neue Summe",self.summe)
    def geldInvestieren(self, wert):
        self.summe += wert
        print("Neue Summe: ",self.summe)


account = Account("Eren Tuna", 123456, 1000)
account.accountInfo()
account.geldAusgeben(1200)
account.geldInvestieren(800)
