from app.animal import Animal
from app.herbivore import Herbivore


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> Herbivore:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health = herbivore.health - 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
