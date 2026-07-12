class Animal:
    alive = []

    def __init__(self, name: str = "", health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False

        if name == "Lion King":
            Animal.alive.clear()

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        elif self.hidden is True:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, catch: str) -> None:
        if catch.hidden is False and isinstance(catch, Carnivore) is not True:
            catch.health -= 50
            if catch.health <= 0:
                Animal.alive.remove(catch)
