class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name: str = name
        self.hidden: bool = hidden
        Animal.alive.append(self)
        self.health = health

    def _get_health(self) -> int:
        return self._health

    def _set_health(self, value: int) -> None:
        self._health = value
        if self._health <= 0:
            Animal.remove_dead(self)

    health = property(_get_health, _set_health)

    @staticmethod
    def remove_dead(animal: "Animal") -> None:
        if animal in Animal.alive:
            Animal.alive.remove(animal)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            f"}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
