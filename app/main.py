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
        return (f"{"{"}Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}{"}"}")


class Carnivore(Animal):

    def bite(self, other: Animal) -> None:
        if other.__class__.__name__ == "Herbivore" and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True
