class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herb_inst: Herbivore) -> None:
        if not (herb_inst.hidden or isinstance(herb_inst, Carnivore)):
            herb_inst.health -= 50
        for i, animal in enumerate(Animal.alive):
            if animal.health <= 0:
                Animal.alive.pop(i)
