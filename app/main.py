from typing import List, Optional

class Animal:
    alive: List['Animal'] = []

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

    def __del__(self) -> None:
        Animal.alive.remove(self)

    def __str__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Carnivore) or target.hidden:
            return
        target.health -= 50
        if target.health <= 0:
            target.die()

lion = Carnivore("Lion King")
rabbit = Herbivore("Susan")

print(len(Animal.alive) == 1)
print(isinstance(Animal.alive[0], Carnivore))

rabbit.hide()
print(rabbit.hidden)

print(rabbit.health == 100)
lion.bite(rabbit)
print(rabbit.health == 50)

rabbit.hide()
lion.bite(rabbit)
print(rabbit.health == 50)

rabbit.hide()
lion.bite(rabbit)
print(rabbit.health == 0)

print(rabbit not in Animal.alive)

pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)
