class Animal:
    # registry of alive animals
    alive = []

    def __init__(self,name: str, health: int=100, hidden: bool=False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    # Magic method to control how the object displays inside a list
    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

class Carnivore(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def bite(self, target: object) -> None:
        if isinstance(target, Herbivore):
            if target in Animal.alive:
                if target.hidden == False:
                    target.health -= 50
                    if target.health <= 0:
                        Animal.alive.remove(target)

class Herbivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def hide(self) -> None:
        self.hidden = not self.hidden


# README.md 14-16
lion = Carnivore("Simba")
print(f"len(Animal.alive) {len(Animal.alive)}")  # == 1 
print(f"{Animal.alive[0].name} is Carnivore {isinstance(Animal.alive[0], Carnivore)}")  # is True

# README.md 24-26
rabbit = Herbivore("Susan")
rabbit.hide()
print(f"rabbit.hidden {rabbit.hidden}")  # is True

# README.md 34-48
lion = Carnivore("Lion King")
rabbit = Herbivore("Susan")
print(f"rabbit.health {rabbit.health}")  # == 100
lion.bite(rabbit)
print(f"rabbit.health {rabbit.health}")  # == 50  # bited

rabbit.hide()
lion.bite(rabbit)
print(f"rabbit.health {rabbit.health}")  # == 50  # lion cannot bite hidden rabbit

rabbit.hide()
lion.bite(rabbit)
print(f"rabbit.health {rabbit.health}")  # == 0  # rabbit is dead

print(f"rabbit in Animal.alive {rabbit in Animal.alive}")  # False
# there is no dead animals in Animal.alive

# README.md 54-57
pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)
# [{Name: Bagira, Health: 100, Hidden: False}, {Name: Kaa, Health: 100, Hidden: False}]
