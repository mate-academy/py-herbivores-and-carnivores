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

    def __str__(self) -> str:
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"

    def __repr__(self) -> str:
        return str(self)


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        elif self.hidden is False:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Herbivore) -> None:
        if isinstance(victim, Herbivore)\
                and victim.health > 0 and not victim.hidden:
            victim.health -= 50
            if victim.health <= 0:
                victim.health = 0
                Animal.alive.remove(victim)
