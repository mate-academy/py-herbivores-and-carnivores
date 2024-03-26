class Animal:
    alive = []

    def __init__(self, name, health=None):
        self.name = name
        self.health = health
        if self.health is None:
            self.health = 100  # Set default health to 100 if not provided
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return (f"{{Name: {self.name},"
                f" Health: {self.health}, Hidden: {self.hidden}}}")

    def die(self):
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
        if self.health <= 0:
            print("Herbivore health is zero or less. Dying...")
            self.die()
            return  # Return after dying to prevent further actions


class Carnivore(Animal):
    def bite(self, animal):
        if isinstance(animal, Carnivore) or animal.hidden:
            return
        print(f"Biting {animal.name}. Health before: {animal.health}")
        animal.health -= 50
        if animal.health <= 0:
            animal.health = 0  # Ensure health is set to zero if less than zero
            animal.die()
        print(f"Health after biting: {animal.health}")
