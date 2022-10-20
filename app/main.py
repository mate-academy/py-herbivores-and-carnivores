class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    @staticmethod
    def check_health(animal: callable) -> None:
        if animal.health <= 0:
            for rip in Animal.alive:
                if rip.name == animal.name:
                    Animal.alive.remove(rip)


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50
            print("bited")
            super().check_health(herbivore)
        else:
            print(f"{self.name} cannot bite hidden {herbivore.name}")
