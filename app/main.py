class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __str__(self) -> str:
        return (f"{self.__class__.__name__}(name={self.name}, "
                f"health={self.health}, hidden={self.hidden})")

    @staticmethod
    def print_alive() -> str:
        alive_animals = []
        for animal in Animal.alive:
            animal_info = (f"{{Name: {animal.name},"
                           f" Health: {animal.health},"
                           f" Hidden: {animal.hidden}}}")
            alive_animals.append(animal_info)
        return f"[{', '.join(alive_animals)}]"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)


# lion = Carnivore("King Lion")
# pantera = Carnivore("Bagira")
# rabbit = Herbivore("Susan")
# print(Animal.print_alive())
