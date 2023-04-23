class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:

        if isinstance(herbivore, Herbivore):
            if herbivore.hidden is False:
                herbivore.health -= 50
            print(f"{self} Can't bite! {herbivore} hid ^_^")

        if herbivore.health <= 0:
            print(f"{herbivore} is dead")
            Animal.alive.remove(herbivore)
