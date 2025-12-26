class Animal:

    alive: list["Animal"] = []

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

    def apply_damage(self, damage_from_bite: int) -> None:
        self.health -= damage_from_bite
        if self.health <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)
            self.health = 0

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Carnivore):
            return
        if isinstance(target, Herbivore):
            if target.hidden:
                return
        target.apply_damage(50)
