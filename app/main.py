class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def __str__(self):
        return f"{self.name}"


class Herbivore(Animal):
    def hide(self):
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(biter: Herbivore) -> None:
        if isinstance(biter, Herbivore):
            if not biter.hidden:
                biter.health -= 50
                if biter.health <= 0:
                    biter.alive.remove(biter)


pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)
