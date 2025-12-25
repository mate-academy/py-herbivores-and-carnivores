class AliveList(list):
    def __repr__(self) -> str:
        return "[" + ", ".join(repr(animal) for animal in self) + "]"


class Animal:
    alive: AliveList = AliveList()

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore_pet: "Herbivore") -> None:
        if isinstance(herbivore_pet, Herbivore) and not herbivore_pet.hidden:
            herbivore_pet.health -= 50
            if herbivore_pet.health <= 0:
                Animal.alive.remove(herbivore_pet)
