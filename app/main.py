class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self) -> list:
        alive_info = []
        for animal in Animal.alive:
            animal_info = {
                "Name": animal.name,
                "Health": animal.health,
                "Hidden": animal.hidden
            }
            alive_info.append(animal_info)
        return alive_info


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Carnivore) or herbivore.hidden:
            pass
        else:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
