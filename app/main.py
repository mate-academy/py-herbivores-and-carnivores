class Animal:
    alive = []

    def __init__(self, name: str, health: int, hidden: bool) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def check_health(self) -> None:
        if self.health <= 0:
            print(f"{self.name} has died.")
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
        print(f"{self.name} {'is hiding' if self.hidden else 'is visible'}.")

class Carnivore(Animal):
    def bite(self, herbivore) -> None:
        if isinstance(herbivore, Carnivore):
            print(f"{self.name} cannot bite another carnivore!")
            return
        if herbivore.hidden:
            print(f"{self.name} cannot bite {herbivore.name}, because it's hiding!")
            return
        herbivore.health -= 50
        print(f"{self.name} bites {herbivore.name}. {herbivore.name}'s health is now {herbivore.health}.")
        herbivore.check_health()
