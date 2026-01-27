class Animal:
    alive = list()

    def __init__(self, name: str, health: int=100) -> None:
        self.name = name
        Animal.alive.append(self)
        self.health = health
        self.hidden = False

    def __str__(self) -> str:
        tostring = "["
        for beast in Animal.alive:
            tostring += ("{Name: " +
                         beast.name +
                         ", Health: " +
                         beast.health +
                         ", Hidden: " +
                         beast.hidden +
                         "}, ")
        tostring[:-2] += "]"
        return tostring


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Herbivore) -> None:
        if not isinstance(prey, Herbivore) or prey.hidden:
            return
        prey.health -= 50
        if prey.health <= 0:
            Animal.alive.remove(prey)
