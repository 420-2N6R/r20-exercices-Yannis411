from math import pi
#1. Ajouter un raise Exception qui lèvera une exception de type TypeError si le type de paramètre passé
#        lors du __init__ n’est pas un int ou float ( vous pouvez utiliser la fonction type() )

#2.	Ajouter un raise Exception qui lèvera une exception de type ValueError  si la valeur du rayon est 
#       égale ou inférieure à 0

#3.	Terminer la propriété rayon

#4.	Ajouter un setter à la propriété rayon. Le setter doit faire les mêmes vérifications que dans 
#       le __init__ afin de s’assurer que le rayon est correct.

#5.	Terminer les propriétés, circonférence, volume et aire qui ont déjà été déclarés dans la classe.
#       (NOTEZ : la valeur de pi à été importer, vous pouvez utilisé pi comme une constante)




class Sphere:
    def __init__(self, pRayon) -> None:
        self._rayon = pRayon

    @property
    def rayon(self) :
        return self._rayon
    @property
    def circonference(self):
        circonférence = 2*pi*self.rayon
        return circonférence

    @property
    def volume(self):
        volume = 4/3 * pi * (self.rayon ** 3)
        return volume
    @rayon.setter
    def rayon(self, pRayon):
        if type(pRayon) != int and float:
            raise TypeError(f"doit être un int ou float")
        elif self.rayon <= 0:
            raise ValueError(f"Doit être au dessus de zero")
    @property
    def aire(self):
        pass


if __name__ == "__main__" :
    cercle = Sphere(-20)    
    cercle.circonference
    cercle.volume
