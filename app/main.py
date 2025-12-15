class Animal:
    alive: list["Animal"] = []

    def __init__(self,
                 name: str,
                 health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def _die(self
             ) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self
                 ) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self
             ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(target: Animal) -> None:
        if not isinstance(target, Herbivore):
            return

        if target.hidden:
            return

        target.health -= 50

        if target.health <= 0:
            target.health = 0
            target._die()
