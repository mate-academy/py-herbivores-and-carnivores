symbol = "{}"


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        result = (f"{symbol[0]}Name: {self.name},"
                  f" Health: {self.health},"
                  f" Hidden: {self.hidden}{symbol[1]}")
        return result


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if herbivore.hidden is False and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
        else:
            print(f"{self.name} cannot bite hidden {herbivore.name}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = not self.hidden
        else:
            self.hidden = False
