class AliveList(list):
    def __repr__(self) -> str:
        return "[" + ", ".join(repr(a) for a in self) + "]"


class Animal:
    alive: AliveList = AliveList()

    def __init__(self,
                 name: str,
                 health: int = 100) -> None:
        self.name = name
        self.health = health
        if self.health > 0:
            Animal.alive.append(self)
        self.hidden = False

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self,
             target: Animal) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden:
            return
        target.health = max(0, target.health - 50)
        if target.health == 0 and target in Animal.alive:
            Animal.alive.remove(target)
