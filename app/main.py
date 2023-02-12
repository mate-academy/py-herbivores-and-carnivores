class Animal:

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        name_str = f"Name: {self.name}, "
        health_str = f"Health: {self.health}, "
        hidden_str = f"Hidden: {self.hidden}"
        return "{" + name_str + health_str + hidden_str + "}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(obj: Herbivore) -> None:
        if isinstance(obj, Herbivore) and not obj.hidden:
            obj.health -= 50
        if obj.health <= 0:
            Animal.alive.remove(obj)
