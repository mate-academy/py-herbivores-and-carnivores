class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: "Herbivore") -> None:
        if isinstance(herbivore, Carnivore):
            print(f"{self.name} cannot bite another carnivore.")
        elif herbivore.hidden:
            print(f"{self.name} cannot bite hidden {herbivore.name}")
        else:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.health = 0
                Animal.alive.remove(herbivore)
