class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.hidden = hidden
        self.health = health
        Animal.alive.append(self)

    def feed(self) -> None:
        if self.health < 100:
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        return 0

    def check_alive(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore (Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Carnivore):
            return
        if prey.hidden:
            return
        prey.health -= 50
        prey.check_alive()


def feed_animals(animals: list[Animal]) -> int:
    return sum(animal.feed() for animal in animals)
