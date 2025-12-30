class Animal:
    # track alive animals
    alive: list["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        # register this instance as alive
        Animal.alive.append(self)

    def __repr__(self) -> str:
        # short formatting to avoid long lines
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        other: "Herbivore",
    ) -> None:
        # only bite Herbivore instances
        if not isinstance(other, Herbivore):
            return
        # do not bite if target is hidden
        if other.hidden:
            return
        # reduce health
        other.health -= 50
        # if dead, set health to 0 and remove from alive list
        if other.health <= 0:
            other.health = 0
            try:
                Animal.alive.remove(other)
            except ValueError:
                pass
