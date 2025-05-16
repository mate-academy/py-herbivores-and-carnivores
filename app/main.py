class Animal:
    alive = []

    def __init__(self, name: str = "", health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}"
                f", Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, animal_victim: Animal) -> Animal:
        if isinstance(animal_victim, Carnivore):
            return animal_victim
        if animal_victim.hidden:
            return animal_victim

        animal_victim.health -= 50
        if animal_victim.health <= 0:
            animal_victim.health = 0
            if animal_victim in Animal.alive:
                Animal.alive.remove(animal_victim)
        return animal_victim


lion = Carnivore("Simba")
pantera = Carnivore("Bagire")
lion.bite(pantera)
print(pantera.health == 100)
print(Animal.alive)

