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

        Animal.alive.append(self)

    def __repr__(self) -> str:
        result = "{" + "Name: {}, Health: {}, Hidden: {}".\
            format(self.name, self.health, self.hidden) + "}"
        return result


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(beast: Herbivore) -> None:
        if isinstance(beast, Herbivore):
            if not beast.hidden:
                beast.health -= 50
            if beast.health <= 0:
                Animal.alive.remove(beast)
