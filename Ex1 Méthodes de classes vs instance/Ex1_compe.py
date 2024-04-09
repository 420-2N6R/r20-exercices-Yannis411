from datetime import datetime

class CompteBancaire :
    
    listeTransaction = []
    def __init__(self, compte_holder, balance=0) :
            self. compte_holder = compte_holder
            self.balance = balance

    def deposer(self, montant):
          self.balance += montant
          CompteBancaire.listeTransaction.append(f"dépot de {montant}")
          print(f"Un dépot à été fait. Transaction de {montant}, nouveau solde de {self.balance}")
    
    def retirer(self, montant):
            if self.balance > montant:
                self.balance -= montant
                print(f"Un retrait à été fait. Transaction de {montant}, nouveau solde de {self.balance}")
                CompteBancaire.listeTransaction.append(f"retrait de {montant}")

            else:
                  print(f"Fond insuffusants")
      
    def aubaine():
          print(f"Épargner 50$ par mois vous donnera un montant de plus de 20 000$ dans 20 ans!")

    @classmethod
    def imprime():
          print()

    @staticmethod
    def __temps_maintenant():
          return datetime.now().strftime("%H:%M:%S")

compte = CompteBancaire(compte_holder ="Alice", balance=1000)
compte.deposer(500)
compte.retirer(200)
