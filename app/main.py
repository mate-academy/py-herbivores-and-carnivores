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

    @classmethod
    def del_animal(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    def die(self) -> None:
        Animal.del_animal()


class Herbivore(Animal):

    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Herbivore) or herbivore.hidden:
            return
        else:
            herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.del_animal()
