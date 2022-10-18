class Animal:

    alive = []
    alive.append()
    def __init__(self, name: str, health: int = 100, ) -> None:
        self.health = health
        self.name = name
        self.hidden = False

    def __str__(self):



class Herbivore(Animal):
    def hide(self):
        self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(biter: Herbivore) -> None:
        if isinstance(biter, Herbivore):
            if not biter.hidden:
                biter.health -= 50
