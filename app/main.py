class Animal:
    alive: list["Animal"] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        if self.health > 0:
            Animal.alive.append(self)

    @classmethod
    def visible(cls) -> list["Animal"]:
        return [a for a in cls.alive if not a.hidden and a.health > 0]

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self,
             other: Animal,
             damage: int = 50) -> None:

        if other.health <= 0:
            return

        if getattr(other, "hidden", False):
            return

        if not isinstance(other, Herbivore):
            return

        other.health = max(0, other.health - damage)

        if other.health == 0 and other in Animal.alive:
            Animal.alive.remove(other)
