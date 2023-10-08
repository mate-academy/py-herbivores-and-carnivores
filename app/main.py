class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:

        self.health = health
        self.name = name
        self.hidden = hidden
        __class__.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def remove_dead_beast(self) -> None:
        if self.health <= 0:
            __class__.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: "Herbivore") -> None:
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
            victim.remove_dead_beast()
