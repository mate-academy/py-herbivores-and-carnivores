class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    def bite(self, target: Herbivore) -> None:
        if target.hidden:
            print(f"{self.name} cannot bite hidden {target.name}")
        elif not isinstance(target, Carnivore):
            print(f"{self.name} can't bite another carnivore.")
        else:
            target.health -= 50
            if target.health <= 0:
                Animal.alive.remove(target)
