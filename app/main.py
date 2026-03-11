class Animal:
    alive: list["Animal"] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def take_damage(self,
                    damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            herbivore: "Herbivore") -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.take_damage(50)
