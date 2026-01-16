class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.hidden = hidden
        self.health = health
        Animal.alive.append(self)
        print(f"{self.name}, total animals: {len(Animal.alive)}")

    def getbitten(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        animal.getbitten()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def getbitten(self) -> None:
        if not self.hidden:
            self.health -= 50
            if self.health <= 0:
                Animal.alive.remove(self)
