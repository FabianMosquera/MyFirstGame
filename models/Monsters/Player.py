from models.Monsters.Mounstro import Mounstro
from models.armas.Sword import Sword

class Player(Mounstro):
    def __init__(self, nombre: str):
        super().__init__(10, Sword(), nombre)

    def recuperarse(self):
        self.VidaActual += 3
        if self.VidaActual > self.VidaMaxima:
            self.VidaActual = self.VidaMaxima
        