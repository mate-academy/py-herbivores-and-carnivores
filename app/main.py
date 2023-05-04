class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Herbivore) -> None:
        if isinstance(animal, Herbivore):
            if animal.hidden is False:
                animal.health -= 50
            print(f"{self} Can't bite! {animal} hid ^_^")

        if animal.health <= 0:
            print(f"{animal} is dead")
            Animal.alive.remove(animal)
