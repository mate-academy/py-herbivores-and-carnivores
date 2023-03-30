class Animal:
    
    alive = []
    
    def __init__(self, name: str, health: int = 100,
                 hidden_attribute: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden_attribute = hidden_attribute
        Animal.alive.append(self)
        
    def __repr__(self) -> str:
        return print( f"{{Name: {self.name},"
               f"Health: {self.health},"
               f"Hidden_atribute: {self.hidden_attribute}}}")
          
class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden_attribute = not self.hidden_attribute

        return self.hidden_attribute
    
    
class Carnivore(Animal):
    
    @staticmethod
    def bite(animal: Animal):
        if isinstance(animal, Herbivore) and animal.hidden_attribute is False:
            animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
