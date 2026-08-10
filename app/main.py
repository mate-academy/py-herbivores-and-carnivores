class Animal:
    alive: list["Animal"] = []

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
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            victim: Animal
    ) -> None:
        if isinstance(victim, Carnivore):
            pass
        elif isinstance(victim, Herbivore) and victim.hidden:
            pass
        else:
            victim.health -= 50
            if victim.health <= 0:
                Animal.alive.remove(victim)
