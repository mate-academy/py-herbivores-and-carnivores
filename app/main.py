class Animal:
    alive = []
    
    def __init__(self, name, hidden=False, health=100):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)
        
    def health_stats(self):
        if (self.health <= 0):
            self.health = 0
            Animal.remove_dead()

    @classmethod
    def remove_dead(cls):
        cls.alive = [animal for animal in cls.alive if animal.health > 0]
    
    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"
        


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore):
        if isinstance(herbivore, Carnivore):
            return "Carnivore cannot bite another carnivor"
        elif herbivore.hidden:
            return "Carnivore cannot bite hidden herbivore"
        herbivore.health -= 50
        herbivore.health_stats()