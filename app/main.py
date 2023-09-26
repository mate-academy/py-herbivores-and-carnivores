class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def update_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        Animal.alive.remove(self)
        self.health = 0

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, target):
        print(not self.hidden)
        if isinstance(target, Herbivore) and not self.hidden:
            target.update_health(50)
