class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(enemy: Herbivore) -> None:
        if isinstance(enemy, Herbivore) and not enemy.hidden:
            enemy.health = enemy.health - 50
            if enemy.health <= 0:
                Animal.alive.remove(enemy)
