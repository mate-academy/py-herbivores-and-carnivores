from __future__ import annotations


class Animal:
    alive: list[Animal] = []

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

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: \
{self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, prey: Herbivore) -> None:
        if not prey.hidden and not isinstance(prey, Carnivore):
            prey.health -= 50
            if prey.health <= 0:
                Animal.alive.remove(prey)


# pantera = Carnivore("Bagira")
# snake = Carnivore("Kaa")
# lion = Carnivore("Lion King")
# print(Animal.alive)
