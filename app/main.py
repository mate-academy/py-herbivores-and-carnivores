class Animal:
    alive: list["Animal"] = []

    def __init__(
        self, name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{'{'}Name: {self.name},"
                f" Health: {self.health}, "
                f"Hidden: {self.hidden}{'}'}")

    @classmethod
    def del_dead_animal(cls, others: "Animal") -> None:
        if others in cls.alive:
            cls.alive.remove(others)


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(other: "Animal") -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health = other.health - 50
        Animal.del_dead_animal(other)
