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

    def __setattr__(self, attr: str, value: int) -> None:
        if attr == "health" and value <= 0 and self in Animal.alive:
            Animal.alive.remove(self)
        super().__setattr__(attr, value)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> bool:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False
        return self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: "Animal") -> int:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
        return other.health
