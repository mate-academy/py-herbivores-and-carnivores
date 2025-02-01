class Animal:
    alive = []

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __str__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def __repr__(self):
        return self.__str__()

class Herbivore(Animal):
        
    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):
        
    def bite(self, cls):
        if isinstance(cls, Carnivore):
            print(f"{self.name} cannot bite another carnivore")
            return
        if cls.hidden:
            print(f"{self.name} cannot bite hidden {cls.name}")
            return
        if cls not in Animal.alive:
            print(f"{cls.name} is dead")
            return
        cls.health -= 50
        print("Bited")
        if cls.health <= 0:
            Animal.alive.remove(cls)
            print(f"{cls.name} has died")
