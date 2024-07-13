class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def check_and_remove(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        name = self.name
        health = self.health
        hidden = self.hidden
        return f"{{Name: {name}, Health: {health}, Hidden: {hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if self.hidden is False else False


class Carnivore(Animal):
    def bite(self, obj: Herbivore) -> None:
        if isinstance(obj, Herbivore) and obj.hidden is False:
            obj.health -= 50
            obj.check_and_remove()
