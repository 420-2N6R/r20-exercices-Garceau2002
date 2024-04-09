from datetime import datetime

class CompteBancaire :
    def __init__(self, compte_holder, balance=0) :
            self. compte_holder = compte_holder
            self.balance = balance

    def deposer(self,montant):
          self.balance += montant
          print(f"${montant} DÉPOSER ; NOUVEAUX SOMME {self.balance}")
          
    
    def retirer(self,montant):
          if montant<= self.balance: 
            self.balance -= montant
            print(f"${montant} Retiré ; NOUVEAUX SOMME {self.balance}")
          else:
            print(f"impossible de retirer somme insufisnate il reste {self.balance} dans ce compte")

    #def aubaine

    @staticmethod
    def __temps_maintenant():
          return datetime.now().strftime("%H:%M:%S")

compte = CompteBancaire("Bruno",1292)
compte.deposer(500)
compte.retirer(200)

