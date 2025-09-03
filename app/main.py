class AnimalList(list):
    def __repr__(self) -> str:
        return "[" + ", ".join(repr(a) for a in self) + "]"


class Animal:
    alive: AnimalList = AnimalList()

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if not isinstance(target, Herbivore):
            return

        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50

        if target.health <= 0:
            Animal.alive.remove(target)
