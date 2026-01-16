class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage. Health: {self.health}")

        if self.health == 0:
            self.die()

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)
        print(f"{self.name} is dead.")

    def is_alive(self) -> bool:
        return self.health > 0

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore):
            if herbivore.hidden:
                print(f"{self.name} cannot bite {herbivore.name} "
                      f"because they are hidden.")
            else:
                herbivore.take_damage(50)
                print(f"{self.name} bit {herbivore.name}. "
                      f"{herbivore.name} s health: {herbivore.health}"
                      )
        else:
            print(f"{self.name} cannot bite another carnivore.")
