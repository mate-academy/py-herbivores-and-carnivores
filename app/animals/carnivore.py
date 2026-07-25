from app.animals.animal import Animal
from app.animals.herbivore import Herbivore


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Herbivore):
            return

        if herbivore.hidden:
            return

        herbivore.health -= 50

        if herbivore.health <= 0:
            herbivore.health = 0
            herbivore._die()
