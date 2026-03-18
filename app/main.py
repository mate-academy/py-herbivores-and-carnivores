class Animal:
    alive: list[Animal] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Carnivore(Animal):

    def bite(self, victim: Carnivore | Herbivore) -> None:
        if victim.hidden:
            print(f"{victim.name} is hiding")
            return None
        if isinstance(victim, Carnivore):
            print(f"{victim.name} is Carnivore")
            return None
        else:
            victim.health -= 50
        if victim.health <= 0:
            Animal.alive.remove(victim)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
