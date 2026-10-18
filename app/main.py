from __future__ import annotations


class Animal():

    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            health: int | float = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        self.is_alive()

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def is_alive(self) -> None:
        if self.health > 0:
            self.update_alive(True)
        else:
            self.update_alive(False)

    def update_alive(self, is_alive: bool) -> None:
        if is_alive and self not in Animal.alive:
            Animal.alive.append(self)
        elif not is_alive and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health = max(0, herbivore.health - 50)
            herbivore.is_alive()
