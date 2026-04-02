class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{\"Name\": \"{self.name}\", \"Health\": {self.health}, \"Hidden\": {self.hidden}}}"

    def update_health(self, amount: int) -> None:
        self.health += amount
        if self.health <= 0:
            print(f"{self.name} is died!")
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Herbivore) -> None:
        if not isinstance(prey, Herbivore):
            print(f"{prey.name} is not a Herbivore!")
        elif prey.hidden:
            print(f"The prey {prey.name} is hidden!")
        else:
            print(f"The prey {prey.name} is bitten!")
            prey.update_health(-50)
