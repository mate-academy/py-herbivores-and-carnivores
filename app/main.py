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
                f"Health: {self.health}, Hidden: {self.hidden}}}")

    def check_health(self) -> None:
        if self.health <= 0:
            self.health = 0
            Animal.alive.remove(self)


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health = other.health - 50
                other.check_health()
            else:
                pass


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
