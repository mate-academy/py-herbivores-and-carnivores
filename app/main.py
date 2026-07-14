class Animal:
    alive = []

    def __init__(self, name: str = "", health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, catch: Herbivore) -> None:
        if catch.health > 0:
            if catch.hidden is False and not isinstance(catch, Carnivore):
                catch.health -= 50
                if catch.health <= 0:
                    Animal.alive.remove(catch)
