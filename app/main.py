class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        part1 = f"{{Name: {self.name}, "
        part2 = f"Health: {self.health}, Hidden: {self.hidden}}}"
        return part1 + part2

    def dead(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if not target.hidden and isinstance(target, Herbivore):
            target.health -= 50
            if target.health <= 0:
                target.dead()
