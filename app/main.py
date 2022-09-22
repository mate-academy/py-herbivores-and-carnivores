class Animal:

    alive = []

    def __repr__(self) -> str:
        return f'{{Name: {self.name}, ' \
               f'Health: {self.health}, ' \
               f'Hidden: {self.hidden}}}'

    def __init__(self, name, health=100, hidden=False):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(target: Animal) -> None:
        if not target.hidden and not isinstance(target, Carnivore):
            target.health -= 50

        if target.health <= 0:
            Animal.alive.remove(target)
