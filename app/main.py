class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def check_health(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}"
                )

    @classmethod
    def __str__(cls) -> str:
        return f"[{", ".join(map(str, cls.alive))}]"


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, target: Animal) -> bool:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            target.check_health()
