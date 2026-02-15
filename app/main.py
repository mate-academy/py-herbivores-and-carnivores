class Animal:
    alive: list["Animal"] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 ) -> None:
        Animal.alive.append(self)
        self.name = name
        self.health = health
        self.hidden = False

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
            victim: "Animal",
    ) -> None:
        if not isinstance(victim, Herbivore):
            return

        if victim.hidden:
            return

        victim.health -= 50
        if victim.health <= 0:
            Animal.alive.remove(victim)
