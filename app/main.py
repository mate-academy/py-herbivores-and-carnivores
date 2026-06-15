class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden:
            bool = False
    ) -> None:
        self.name = name
        self.hidden = hidden
        self.health = health
        Animal.alive.append(self)

    def is_alive(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f""
                f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            prey.is_alive()
            return None
        else:
            return None
