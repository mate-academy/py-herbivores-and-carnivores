class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def die(self) -> None:
        Animal.alive.remove(self)

    def bite_health(self, bite_damage: int) -> None:
        self.health -= bite_damage
        if self.health <= 0:
            self.die()


class Carnivore(Animal):
    @staticmethod
    def bite(target: Animal) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.bite_health(50)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
