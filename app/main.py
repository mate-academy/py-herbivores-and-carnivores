# write your code here
class Animal:
    alive = []  # list of all alive animals

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        # Custom string representation for printing
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def take_damage(self, amount):
        """Reduce health by amount and remove from alive if dead."""
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        """Toggle hidden status"""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target):
        """Bite a herbivore, reducing its health by 50 if not hidden."""
        if isinstance(target, Herbivore) and not target.hidden:
            target.take_damage(50)
        animal.health -= 50

        if animal.health <= 0:
            animal.health = 0
            animal.die()
