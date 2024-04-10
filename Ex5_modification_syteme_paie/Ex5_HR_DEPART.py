#On veut calculer la paie des employes
#Mais on a des employés payés à la semaine pour un montant fixe
#On a aussi des employés payés à la semaine pour un montant fixe ET qui ont aussi une commission 
#On a aussi des employés payés à l'heure

from abc import ABC,abstractmethod

class Systeme_de_paie:
    def calculer_paie(self, employes):
        print("Calcul de la paie des employes")
        print("==============================")
        for employe in employes:
            print(f'Paie de: {employe.id} - {employe.nom}')
            print(f' - montant net de:  {employe.calculer_paie()}')
            print('')
            
class Employe(ABC):
    
    liste_employes = []
    
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        Employe.liste_employes.append(self)
        
    @abstractmethod
    def calculer_paie():
        pass
    
class Employe_salarie(Employe):
    def __init__(self, id, nom, salaire_par_semaine):
        super().__init__(id, nom)
        self._salaire_par_semaine = salaire_par_semaine
        
    def calculer_paie(self):
        return self._salaire_par_semaine
    @property
    def salaire_par_semaine(self):
        return self._salaire_par_semaine
    @salaire_par_semaine.setter
    def salaire_par_semaine(self):
        try:
            if type(self._salaire_par_semaine) == float:
                print(f"Le salaire a changé")
        except TypeError:
            print(f"Vous devez entrer une valeur float")
class Employe_heure(Employe):  
    def __init__(self, id, nom, heures_travaillees, taux_horaire):
        super().__init__(id, nom)
        self._heures_travaillees = heures_travaillees
        self._taux_horaire = taux_horaire

    @property
    def heures_travaillee(self):
        return self._heures_travaillees
    @heures_travaillee.setter
    def heures_travaillees(self):
        try:
            if type(self._heures_travaillees) == float:
                print(f"Les heures ont changés")
        except TypeError:
            print(f"Vous devez entrer une valeur float")


    @property
    def taux_horaire(self):
        return self._taux_horaire    
    @taux_horaire.setter
    def taux_horaie(self):
        try:
            if type(self._taux_horaire) == float:
                print(f"Le taux horaire ont changés")
        except TypeError:
            print(f"Vous devez entrer une valeur float")


    def calculer_paie(self):
        return self.heures_travaillees * self.taux_horaire
    
class Employe_commission(Employe_salarie):  
    def __init__(self, id, nom, _salaire_par_semaine, commission):
        super().__init__(id, nom, _salaire_par_semaine)
        self._commission = commission

    @property
    def commission(self):
        return self._commission
    @commission.setter
    def commission(self):
        try:
            if type(self._commission) == float:
                print(f"La commission a changés")
        except TypeError:
            print(f"Vous devez entrer une valeur float")
    
    
    @property
    def salaire_par_semaine(self):
        return self._salaire_par_semaine    
    @salaire_par_semaine.setter
    def salaire_par_semaine(self):
        try:
            if type(self._salaire_par_semaine) == float:
                print(f"Le taux horaire ont changés")
        except TypeError:
            print(f"Vous devez entrer une valeur float")  

    def calculer_paie(self):
        salaire_fixe = super().calculer_paie()
        return salaire_fixe + self.commission
        
employe_salarie1 = Employe_salarie(1, 'Marc Tremblay', 2100)
employe_heure1 = Employe_heure(2,'Pierre Jonhson', 40, 22)
employe_commission1 = Employe_commission(3, 'Luc Toupin', 1400, 600)
#employex = Employe(4,'Lucie Rangers')


systeme_de_paie_hr = Systeme_de_paie()
systeme_de_paie_hr.calculer_paie([employe_salarie1,employe_heure1,employe_commission1])


    
     