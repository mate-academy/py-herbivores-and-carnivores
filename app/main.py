class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        self.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, ofiara: Animal) -> None:
        if ofiara.hidden:
            return

        if isinstance(ofiara, Carnivore):
            return
        ofiara.health -= 50

        if ofiara.health <= 0:
            Animal.alive.remove(ofiara)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")
