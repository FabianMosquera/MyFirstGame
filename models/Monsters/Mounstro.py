from models.armas.Weapon import Weapon

class Mounstro():

    def __init__(self, VidaMaxima: int, arma: 'Weapon', nombre: str):
        self.VidaMaxima = VidaMaxima
        self.arma = arma
        self.nombre = nombre
        self.VidaActual = VidaMaxima

    def getAttackPoitns(self):
        return self.arma.getAttackPoints()

    def DañoRecibido(self, mounstro: 'Mounstro'):
        self.VidaActual -= mounstro.getAttackPoitns()
        if self.VidaActual < 0:
            self.VidaActual = 0:

    def Atacar(self, mounstroAparece: 'Mounstro'):
        mounstroAparece.DañoRecibido(self)
