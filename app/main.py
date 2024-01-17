class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def die(self):
        Animal.alive.remove(self)


def format_animal_list(animal_list):
    return [str(animal) for animal in animal_list]


class Herbivore(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.hidden = False

    def hide(self):
        self.hidden = not self.hidden

    def __str__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Carnivore(Animal):
    @staticmethod
    def bite(target):
        if isinstance(target, Carnivore) or target.hidden:
            return
        target.health -= 50
        if target.health <= 0:
            target.die()

    def __str__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"
