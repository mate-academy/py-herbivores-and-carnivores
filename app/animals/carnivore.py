from app.animals.base.animal import Animal
from app.animals.herbivore import Herbivore


class Carnivore(Animal):

    @staticmethod
    def bite(
        animal: Animal
    ) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
