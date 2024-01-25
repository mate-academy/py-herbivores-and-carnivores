class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}"



class Herbivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.hidden = False

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(target: Herbivore) -> None:
        if target.hidden:
            return
        target.health -= 50
        if target.health <= 0:
            target.die()
