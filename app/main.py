class Animal:

    alive: list["Animal"] = []

    def __init__(self, name: str, *args) -> None:
        self.name = name
        if args != ():
            self.health = args[0]
        else:
            self.health = 100
        Animal.alive.append(self)
        self.hidden = False

    @property
    def health(self) -> None:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = value
        if self._health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        represent = (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )
        return represent


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health = prey.health - 50
            print(f"{prey.name} is bitten")
