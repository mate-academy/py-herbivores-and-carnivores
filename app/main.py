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

    def __repr__(self) -> None:
        return "{{Name: {}, Health: {}, Hidden: {}}}".format(
            self.name,
            self.health,
            self.hidden
        )


class Carnivore(Animal):
    def bite(self, other: "Animal") -> None:
        if isinstance(other, Carnivore):
            return
        elif other.hidden:
            return

        other.health -= 50
        if other.health <= 0:
            other.health = 0
            Animal.alive.remove(other)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
