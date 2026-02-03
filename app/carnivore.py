from app.animal import Animal
from app.herbivore import Herbivore


class Carnivore(Animal):

    @staticmethod
    def bite(animal: Animal) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50

            if animal.health <= 0:
                Animal.alive.remove(animal)
