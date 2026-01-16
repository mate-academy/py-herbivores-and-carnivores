class Animal:

    alive: list["Animal"] = []

    def __init__(
            self,
            name: str = "animal",
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        if health > 0:
            Animal.alive.append(self)

    def die(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def bite(self, victim: Herbivore) -> None:
        if not isinstance(victim, Herbivore):
            return
        if victim.hidden:
            return

        victim.health = max(victim.health - 50, 0)

        if victim.health == 0:
            victim.die()
