class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self. hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        s_nm = self.name
        s_ht = self.health
        s_hi = self.hidden
        return f"{{Name: {s_nm}, Health: {s_ht}, Hidden: {s_hi}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @classmethod
    def bite(cls, animal: Animal) -> None:
        if animal.hidden is False and not isinstance(animal, Carnivore):
            animal.health -= 50
        if animal.health <= 0:
            super().alive.remove(animal)
