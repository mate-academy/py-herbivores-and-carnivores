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

    def check_is_alive(self) -> bool:

        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)
            return False
        return True

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )


class Herbivore(Animal):

    def hide(self) -> bool:
        if self.hidden:
            self.hidden = not self.hidden
            return self.hidden
        self.hidden = True
        return self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: None) -> None:
        if isinstance(herbivore, Herbivore):
            if herbivore.hidden is False:
                herbivore.health -= 50
                herbivore.check_is_alive()
