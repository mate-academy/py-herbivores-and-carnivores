class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal):
        if not isinstance(target, Herbivore) or target.hidden:
            return
        target.health -= 50
        if target.health <= 0:
            target.health = 0
            try:
                Animal.alive.remove(target)
            except ValueError:
                pass
