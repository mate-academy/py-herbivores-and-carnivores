class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self._health = health
        self.hidden = hidden
        self.add_to_alive(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = value
        if self._health <= 0:
            self.remove_from_alive(self)

    @classmethod
    def add_to_alive(cls, animal: Animal) -> None:
        if animal not in cls.alive:
            cls.alive.append(animal)

    @classmethod
    def remove_from_alive(cls, animal: Animal) -> None:
        if animal in cls.alive:
            cls.alive.remove(animal)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: Herbivore) -> None:
        if not victim.hidden and isinstance(victim, Herbivore):
            victim.health -= 50
