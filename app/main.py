class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{" + f"Name: {self.name}, " \
                     f"Health: {self.health}, " \
                     f"Hidden: {self.hidden}" + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, herb_is_bite: Herbivore) -> Herbivore:
        if herb_is_bite.hidden is False and\
                isinstance(herb_is_bite, Herbivore):
            herb_is_bite.health -= 50
        if herb_is_bite.health <= 0:
            for index in range(len(self.alive)):
                if self.alive[index] == herb_is_bite:
                    self.alive.pop(index)
        return herb_is_bite
