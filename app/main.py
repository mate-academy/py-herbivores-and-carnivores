class Animal:
    alive = []

    def __init__(self,
                 name: str = None,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def dead(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Herbivore) -> None:
        if victim.hidden or not isinstance(victim, Herbivore):
            return
        victim.health -= 50
        if victim.health <= 0:
            victim.dead()
