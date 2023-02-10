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
        return f"{{Name: {self.name}," \
               f" Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbiv_obj: Herbivore) -> None:
        if isinstance(herbiv_obj, Herbivore) and herbiv_obj.hidden is False:
            herbiv_obj.health -= 50
            if herbiv_obj.health <= 0:
                Animal.alive.remove(herbiv_obj)
