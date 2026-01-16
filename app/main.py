class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def became_dead(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            "{"
            f"Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}"
            "}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50

            if animal.health <= 0:
                animal.became_dead()
