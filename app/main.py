class AnimalList(list):
    def __repr__(self):
        items = []
        for animal in self:
            items.append(
                f"{{Name: {animal.name}, Health: {animal.health}, Hidden: {animal.hidden}}}"
            )
        return "[" + ", ".join(items) + "]"


class AnimalMeta(type):
    def __setattr__(cls, name, value):
        if name == "alive" and not isinstance(value, AnimalList):
            value = AnimalList(value)
        super().__setattr__(name, value)


class Animal(metaclass=AnimalMeta):
    alive = AnimalList()

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def take_damage(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal):
        if isinstance(target, Herbivore) and not target.hidden:
            target.take_damage(50)
