class Animal:
    alive = []  # Class attribute to track all alive animals

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __del__(self):
        Animal.alive.remove(self)  # Remove the animal from the alive list when it dies

    @classmethod
    def remove_dead(cls, animal):
        """Remove dead animals from the alive list."""
        if animal.health <= 0:
            cls.alive.remove(animal)

    def __str__(self):
        """Return a custom string for Animal's state."""
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        """Toggle the 'hidden' state."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore):
        """Carnivores can bite herbivores, reducing their health."""
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.__del__()  # Remove from alive if health drops to 0
        elif isinstance(herbivore, Carnivore):
            print("Carnivores cannot bite other carnivores.")
        elif herbivore.hidden:
            print(f"{herbivore.name} is hiding. Cannot bite.")


# Example usage
lion = Carnivore("Simba")
rabbit = Herbivore("Susan")

# Test Animal.alive list after creation
print(len(Animal.alive))  # Should print 2
print(isinstance(Animal.alive[0], Carnivore))  # Should print True

# Herbivore hide and bite tests
rabbit.hide()
print(rabbit.hidden)  # True

lion.bite(rabbit)  # Should reduce rabbit's health to 50
print(rabbit.health)  # Should print 50

rabbit.hide()  # Rabbit hides again
lion.bite(rabbit)  # Should not affect rabbit's health
print(rabbit.health)  # Should still print 50

lion.bite(rabbit)  # Should reduce health to 0, and rabbit dies
print(rabbit.health)  # Should print 0
print(rabbit in Animal.alive)  # Should print False, as rabbit is dead

# Print Animal.alive list
pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)  # Should print the alive carnivores in the specified format

