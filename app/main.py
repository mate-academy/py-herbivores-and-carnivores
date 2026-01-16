class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def new_alive_list(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, prey: "Animal") -> None:
        if isinstance(prey, Herbivore) and not prey.hidden and self != prey:
            prey.health -= 50
            if prey.health <= 0:
                Animal.new_alive_list()
