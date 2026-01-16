from app.animals.animal import Animal
from app.animals.herbivore import Herbivore


class Carnivore(Animal):

    @staticmethod
    def bite(other: Herbivore) -> None:
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
                other.health = max(other.health, 0)
                if other.health == 0:
                    Animal.alive.remove(other)
