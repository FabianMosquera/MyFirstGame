from models.armas.Sword import Sword
from models.Monsters.Mounstro import Mounstro


class Orco(Mounstro):

    def __init__(self):
        super().__init__(5, Sword(), "Anhujuju")
