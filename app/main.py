class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return str({
            "Name": self.name,
            "Health": self.health,
            "Hidden": self.hidden,
        }).replace("'", "")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if not other.hidden and not isinstance(other, Carnivore):
            other.health -= 50
            if other.health <= 0:
                other.health = 0
                Animal.alive.remove(other)
