from app.animals.animal import Animal
from app.animals.herbivore import Herbivore


class Carnivore(Animal):

    def bite(self, pray: Herbivore) -> None:
        if not isinstance(pray, Herbivore):
            return
        if not pray.hidden:
            pray.health -= 50
            if pray.health <= 0:
                super().alive.remove(pray)
