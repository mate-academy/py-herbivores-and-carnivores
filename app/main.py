class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.__hidden = False
        Animal.alive.append(self)

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}")

    def _toggle_hidden(self) -> None:
        self.__hidden = not self.__hidden

    @property
    def hidden(self) -> bool:
        return self.__hidden


class Herbivore(Animal):
    def hide(self) -> None:
        self._toggle_hidden()


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden:
            return
        target.take_damage(50)
