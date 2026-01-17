class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    def death(self) -> None:
        if self.health <= 0 and self in self.__class__.alive:
            self.__class__.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50
            prey.death()
