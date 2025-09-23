class Animal:
    alive = []

    def __init__(
        self,
        name: str = "",
        health: int = 100,
        hidden: bool = False,
    ):
        self._health = 0
        self.health = health
        self.name = name
        self.hidden = hidden

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value_health):
        self._health = value_health

        if self._health <= 0:
            Animal.alive.remove(self)
        else:
            if self not in Animal.alive:
                Animal.alive.append(self)

    def __repr__(self):
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal):
        if isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50
