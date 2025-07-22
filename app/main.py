class AliveList(list):
    def __repr__(self) -> str:
        return str([repr(animal) for animal in self])


class Animal:
    alive: AliveList = AliveList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def _update_alive(cls) -> None:
        cls.alive = AliveList(
            [animal for animal in cls.alive if animal.health > 0]
        )

    def _check_health(self) -> None:
        if self.health <= 0:
            self.health = 0
            Animal._update_alive()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            target._check_health()
