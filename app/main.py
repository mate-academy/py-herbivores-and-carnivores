class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.hidden = hidden
        self.alive = True
        self.name = name
        Animal.alive.append(self)

    def check_alive(self) -> None:
        if self.health < 1:
            self.alive = False
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: object) -> None:
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
        victim.check_alive()
