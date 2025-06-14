class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def take_damage(self, amount: int) -> int:
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def is_alive(self) -> None:
        return self in Animal.alive

    def __str__(self) -> None:
        return (f"{{Name: {self.name}, Health:"
                f" {self.health}, Hidden: {self.hidden}}}")

    def __repr__(self) -> None:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: bool) -> bool:
        if isinstance(target, Herbivore) and not target.hidden:
            target.take_damage(50)
