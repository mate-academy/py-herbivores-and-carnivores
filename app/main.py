class Animal:
    alive = []

    def __init__(self, name: str, *args: int) -> None:
        self.name = name
        self.health = args[0] if args else 100
        self.hidden = False
        Animal.alive.append(self)

    def check_health(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: Herbivore) -> None:
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
            victim.check_health()
