class Animal:
    alive = []
    default_health = 100

    def __init__(self, name: str, health: int = None) -> None:
        self.name = name
        self.health = health if health is not None else self.default_health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Carnivore(Animal):
    def check_is_alive(self, animal: Animal) -> None:
        if animal.health <= 0:
            super().alive.remove(animal)

    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            self.check_is_alive(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
