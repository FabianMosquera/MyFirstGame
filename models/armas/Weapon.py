class Weapon():

    @abc.abstractclassmethod
    def getAttackPoints(self):
        pass

    @abc.abstractclassmethod
    def __str__(self):
        pass
