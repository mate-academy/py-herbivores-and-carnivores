from typing import Any, ClassVar, List


class AliveList:
    def __init__(self) -> None:
        self._animals: List["Animal"] = []

    def append(self, animal: "Animal") -> None:
        self._animals.append(animal)

    def remove(self, animal: "Animal") -> None:
        self._animals.remove(animal)

    def __contains__(self, item: object) -> bool:
        return item in self._animals

    def __len__(self) -> int:
        return len(self._animals)

    def __getitem__(self, index: int) -> "Animal":
        return self._animals[index]

    def __iter__(self) -> None:
        return iter(self._animals)

    def __str__(self) -> str:
        return str([repr(animal) for animal in self._animals])

    def __repr__(self) -> str:
        return self.__str__()


class Animal:
    alive: ClassVar[AliveList] = AliveList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        if self.health > 0:
            Animal.alive.append(self)

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "health":
            value = max(0, value)
            if hasattr(self, "health") and value == 0 and self in Animal.alive:
                Animal.alive.remove(self)
        super().__setattr__(key, value)

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
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
