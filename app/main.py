class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def delete_from_alive(self):
        self.__class__.alive.pop(self.__class__.alive.index(self))


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(grass_feeding: Herbivore) -> None:
        if isinstance(grass_feeding, Herbivore) and not grass_feeding.hidden:
            grass_feeding.health -= 50
            if grass_feeding.health <= 0:
                grass_feeding.delete_from_alive()
