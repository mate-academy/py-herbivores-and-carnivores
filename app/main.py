class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def remove_dead(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: int) -> None:
        if isinstance(other, Carnivore) or other.hidden:
            return
        other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
            Animal.remove_dead()
