from __future__ import annotations
from app.anilmal.animal_base import Animal
from app.anilmal.herbivore import Herbivore


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> Animal:
        if isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50

        if animal.health <= 0:
            Animal.alive.remove(animal)

        return animal
