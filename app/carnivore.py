from app.herbivore import Herbivore
from app.animal import Animal


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health = max(0, animal.health - 50)
            if animal.health == 0 and animal in Animal.alive:
                Animal.alive.remove(animal)
