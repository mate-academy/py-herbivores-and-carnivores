class Animal:

    hidden = False
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        info_animal = f"Name: {self.name}," \
                      f" Health: {self.health}," \
                      f" Hidden: {self.hidden}"
        return "{" + f"{info_animal}" + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Animal) -> None:
        if isinstance(victim, Herbivore):
            if victim.hidden is False:
                victim.health -= 50
                if victim.health <= 0:
                    Animal.alive.remove(victim)
