class Animal:
    alive = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        name = self.name
        health = self.health
        hidden = self.hidden
        f_string = f"Name: {name}, Health: {health}, Hidden: {hidden}"
        return "{" + f_string + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if not other.hidden and not isinstance(other, Carnivore):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
