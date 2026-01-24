class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        health = self.health
        name = self.name
        hidden = self.hidden
        return f"{{Name: {name}, Health: {health}, Hidden: {hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50
                if animal.health <= 0:
                    animal.die()
