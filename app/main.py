class Animal:
    alive = []
    hidden = False

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = hidden) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}," \
               f" Health: {self.health}, Hidden: {self.hidden}}}"


class Carnivore(Animal):

    def carnivore(self, name: str) -> None:
        super().__init__(name)

    @staticmethod
    def bite(beast: Animal) -> None:
        if isinstance(beast, Herbivore) and beast.hidden is False:
            beast.health -= 50
        if beast.health <= 0:
            Animal.alive.remove(beast)


class Herbivore(Animal):

    def herbivore(self, name: str) -> None:
        super().__init__(name)

    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False
