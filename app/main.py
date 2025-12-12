from typing import List, Any, Type, TYPE_CHECKING

if TYPE_CHECKING:
    AnimalType = "Animal"
    HerbivoreType = Type["Herbivore"]
    CarnivoreType = Type["Carnivore"]
else:
    AnimalType = Any
    HerbivoreType = Any
    CarnivoreType = Any


class Animal:
    alive: List[AnimalType] = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:
        self.health: int = health
        self.name: str = name
        self.hidden: bool = False

        Animal.alive.append(self)

    def _die(self) -> None:
        Animal.alive.remove(self)

    def set_health(
            self,
            health_change: int
    ) -> None:
        self.health += health_change

        if self.health <= 0:
            self.health = 0
            self._die()

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(
            self,
            target_animal: "Herbivore"
    ) -> None:
        if isinstance(target_animal, Carnivore):
            return

        if target_animal.hidden:
            return

        target_animal.set_health(-50)
