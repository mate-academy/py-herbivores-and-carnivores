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
        result = f"Name: {self.name}, \
Health: {self.health}, \
Hidden: {self.hidden}"
        return "{" + result + "}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, obj: Animal) -> None:
        if obj.hidden is False and isinstance(obj, Herbivore):
            obj.health -= 50
            if obj.health <= 0:
                Animal.alive.remove(obj)
