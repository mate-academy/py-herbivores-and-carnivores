class Animal:
    alive = []
    def __init__(self,
                 name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)
    
    def __repr__(self) -> str:
        return ("{"+f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}"+"}")

class Herbivore(Animal):
    def __init__(self,
                 name: str) -> None:
        super().__init__(name)

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def __init__(self,
                 name: str) -> None:
        super().__init__(name)
    
    def bite(self,
             animal: Animal) -> None:
        if animal in Animal.alive and not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)