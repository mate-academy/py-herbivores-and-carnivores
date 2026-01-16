class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        nm = self.name
        hl = self.health
        hn = self.hidden

        return f"{{Name: {nm}, Health: {hl}, Hidden: {hn}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Herbivore) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50

        if animal.health <= 0:
            Animal.alive.remove(animal)
