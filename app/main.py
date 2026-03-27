class Animal(object):
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self) -> str:
        return (f"Name = {self.name},\n"
                f"Current hp = {self.health},\n"
                f"Hiding? = {'Yes' if self.hidden == True else 'No'}\n")

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden

    def __isub__(self) -> Animal:
        self.health -= 50
        if self.health <= 0:
            Animal.alive.remove(self)
        return self


class Carnivore(Animal):
    @staticmethod
    def bite(target: Herbivore) -> None:
        if isinstance(target, Herbivore) and target.hidden is False:
            target.__isub__()
