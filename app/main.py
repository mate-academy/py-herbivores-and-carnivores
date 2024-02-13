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


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herb_inst: Herbivore) -> Herbivore:
        if not (herb_inst.hidden and isinstance(herb_inst, Carnivore)):
            herb_inst.health -= 50
            return herb_inst












