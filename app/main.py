class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return ("{{Name: {}, Health: {}, Hidden: {}}}"
                .format(self.name, self.health, self.hidden))


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = False if self.hidden else True


class Carnivore(Animal):
    def bite(self, animal: Herbivore) -> None:
        if animal.hidden or isinstance(animal, Carnivore):
            return
        animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
