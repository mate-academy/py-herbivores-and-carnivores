class Animal:
    alive = []
    hidden = False

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herb_obj: Herbivore) -> None:
        if isinstance(herb_obj, Herbivore):
            if not herb_obj.hidden:
                herb_obj.health -= 50

        if herb_obj.health <= 0:
            Animal.alive.remove(herb_obj)
