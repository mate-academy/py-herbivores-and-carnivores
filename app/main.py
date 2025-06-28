class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Carnivore):
            return

        if not herbivore.hidden:
            herbivore.health -= 50

        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)


if __name__ == "__main__":
    # lion = Carnivore("Lion King")
    # print(len(Animal.alive))
    # print(isinstance(Animal.alive[0], Carnivore))
    #
    # rabbit = Herbivore("Susan")
    # rabbit.hide()
    # is_hidden = rabbit.hidden
    # print(is_hidden)

    lion = Carnivore("Lion King")
    rabbit = Herbivore("Susan")

    print(Animal.alive)

    print(rabbit.health)
    lion.bite(rabbit)
    print(rabbit.health == 50)

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health == 50)

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health == 0)

    # print(rabbit in Animal.alive)
