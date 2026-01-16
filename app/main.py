class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def take_damage(self) -> None:
        if self.hidden:
            pass
        else:
            if self.health <= 50:
                if self in Animal.alive:
                    self.alive.remove(self)
                else:
                    pass
            else:
                self.health -= 50


class Carnivore(Animal):
    def bite(self, victim: Animal) -> None:
        if isinstance(victim, Carnivore):
            pass
        if isinstance(victim, Herbivore):
            victim.take_damage()
