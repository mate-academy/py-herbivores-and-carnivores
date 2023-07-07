class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        presentation_text = {
            "Name": self.name,
            "Health": self.health,
            "Hidden": self.hidden
        }
        return str(presentation_text).replace("'", "")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if self.hidden is False \
            else False


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if animal.hidden is not True \
                and isinstance(animal, Carnivore) is False:
            animal.health -= 50
            if animal.health <= 0:
                animal.health = 0
                self.alive.remove(animal)
