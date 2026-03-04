class Animal():

    alive: list["Animal"] = []

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
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if herbivore.hidden is True:
            print(f"{self.name} cannot bite hidden {herbivore.name}")
            return
        else:
            if herbivore.health > 0:
                if isinstance(herbivore, Herbivore):
                    herbivore.health -= 50
                    print("bited")
                    if herbivore.health <= 0:
                        Animal.alive.remove(herbivore)
                        print(f"{herbivore.name} is dead")
