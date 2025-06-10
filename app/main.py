class Animal:
    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    alive = []


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if (isinstance(target, Herbivore)
                and not target.hidden
                and target.health > 0):
            target.health -= 50
            if target.health <= 0 and target in Animal.alive:
                Animal.alive.remove(target)
        elif isinstance(target, Herbivore) and target.hidden:
            print(f"{self.name} cannot bite hidden {target.name}")
        elif isinstance(target, Carnivore):
            print(f"{self.name} cannot bitee {target.name}")
