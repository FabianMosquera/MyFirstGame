from models.armas.Weapon import Weapon

class Sword(Weapon):

    @abc.abstractclassmethod
    def getAttackPoints(self):
        return 3

    @abc.abstractclassmethod
    def __str__(self):
        return "Espada"
