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
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = False if self.hidden else True


class Carnivore(Animal):
    def bite(self, herbivore_obj: Herbivore) -> None:
        if isinstance(herbivore_obj, Herbivore) and not herbivore_obj.hidden:
            herbivore_obj.health -= 50
            if herbivore_obj.health <= 0:
                Animal.alive.remove(herbivore_obj)
