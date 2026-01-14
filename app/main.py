class Animal:
    alive = []
    animal = {}

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.animal[self.name] = self
        Animal.alive.append(self)

    def __repr__(self) -> None:
        return (f"{{Name: {self.name}"
                f", Health: {self.health}"
                f", Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> Animal:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True
        return self


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> Animal:
        if isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50

        if animal.health <= 0 and animal in Animal.alive:
            Animal.alive.remove(animal)

        return animal
