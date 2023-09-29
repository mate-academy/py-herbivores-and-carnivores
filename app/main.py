class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def __repr__(self) -> str:
        data_string = ", ".join([f"{key.capitalize()}: {str(value)}"
                                 for key, value in self.__dict__.items()])
        return f"{{{data_string}}}"

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(prey: Herbivore) -> None:
        if not prey.hidden and not isinstance(prey, Carnivore):
            prey.take_damage(50)
