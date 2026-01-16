class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(enemy: Animal) -> None:
        if not enemy.hidden and not isinstance(enemy, Carnivore):
            enemy.health -= 50
        if enemy.health <= 0:
            if enemy in enemy.alive:
                enemy.__class__.alive.remove(enemy)
