from ..animal.animal import Animal
from ..herbivore.herbivore import Herbivore


class Carnivore(Animal):
    def bite(self, victim: Herbivore) -> None:
        if isinstance(victim, Herbivore) and victim.hidden is False:
            victim.health -= 50
            if victim.health < 1:
                Animal.alive.remove(victim)
