class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(Animal(name))

    def __str__(self) -> str:
        return [{Name: {animal.name}, Health: {animal.health}, Hidden: {animal.hidden}} for animal in Animal.alive]

class Herbivore(Animal):

    def __init__(self, name):
        super().__init__(name)
    
    def hide(self) -> None:
        self.hidden = not self.hidden

class Сarnivore(Animal):

    def __init__(self, name):
        super().__init__(name)
    
    def bite(self, other: "Herbivore") -> None
        if other.hidden == False:
            other.health -= 50
        if other.health < 0:
            other.health = 0
    
