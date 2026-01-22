class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str :
        need_return = ""
        need_return += "{" + (f"Name: {self.name}, "
                              f"Health: {self.health}, "
                              f"Hidden: {self.hidden}") + "}"
        return need_return


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(animal: "Animal") -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                for element in Animal.alive:
                    if element.name == animal.name:
                        Animal.alive.remove(element)
