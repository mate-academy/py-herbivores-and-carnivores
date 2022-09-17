class Animal:
    alive = []

    def __init__(self, name, health: int = 100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{" \
               f"Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}" \
               f"}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(victim):
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
        if victim.health <= 0:
            Animal.alive.pop(Animal.alive.index(victim))
