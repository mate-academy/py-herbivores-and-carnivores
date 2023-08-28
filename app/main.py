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
        return str(self.__dict__).replace("'", "").title()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def is_alive(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Carnivore(Animal):
    @staticmethod
    def bite(prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            prey.is_alive()
