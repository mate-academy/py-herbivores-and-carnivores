from app.animal_project.Animal import Animal
from app.animal_project.Herbivore import Herbivore


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        """
        We check that we are biting into a herbivore
        """
        if isinstance(other, Herbivore):
            """
            Check if the rabbit is hidden
            """
            if not other.hidden:
                """
                bite: take away 50 health
                """
                other.health -= 50
                """
                If health drops to 0, the rabbit dies.
                """
                if other.health <= 0:
                    Animal.alive.remove(other)
