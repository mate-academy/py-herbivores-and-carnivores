class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) \
            -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore_object: [Herbivore]) -> None:
        if isinstance(herbivore_object, Herbivore):
            if not herbivore_object.hidden:
                herbivore_object.health -= 50
                if herbivore_object.health <= 0:
                    herbivore_object.alive.remove(herbivore_object)
