class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def death(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if not other.hidden and not isinstance(other, Carnivore):
            other.health -= 50
            Animal.death(other)


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False
