class Animal:
    alive = []

    def __init__(self, name: str):
        self.name: str = name
        self.health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

    def __del__(self):
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: " \
               f"{self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def remove_dead(cls):
        cls.alive = [animal for animal in cls.alive if animal.health > 0]


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.remove_dead()
