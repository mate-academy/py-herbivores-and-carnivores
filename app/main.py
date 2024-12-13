class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def take_damage(self) -> None:
        self.health -= 50
        if self.health <= 0:
            Animal.alive.remove(self)
        return None

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def __str__() -> str:
        return str([repr(animal) for animal in Animal.alive])


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True
        return None


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.take_damage()
