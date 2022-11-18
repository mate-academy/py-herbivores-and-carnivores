from app.Animal import Animal
from app.Herbivore import Herbivore


class Carnivore(Animal):

    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
        if animal.health <= 0:
            self.__class__.alive.remove(animal)
