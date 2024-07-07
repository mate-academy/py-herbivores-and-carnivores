class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:

        self.name = name.title()
        self.health = health
        self.hidden = hidden
        if health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:

        self.hidden = not self.hidden

        for index in range(len(Animal.alive)):
            if Animal.alive[index].name == self.name:
                Animal.alive[index].hidden = self.hidden
                break


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:

        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50

            for index in range(len(super().alive)):
                if Animal.alive[index].name == herbivore.name:
                    if herbivore.health <= 0:
                        del Animal.alive[index]
                    else:
                        Animal.alive[index].health = herbivore.health
                    break
