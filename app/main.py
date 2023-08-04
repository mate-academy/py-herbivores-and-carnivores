from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden: bool = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}}}"
        )

    def set_health(self, new_health: int) -> None:
        self.health = max(new_health, 0)
        if self.health <= 0:
            self.__die()

    def __die(self) -> None:
        self.alive.remove(self)

    @classmethod
    def get_all_alive(cls) -> List["Animal"]:
        return cls.alive


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: "Animal") -> None:
        if isinstance(target, Carnivore) or target.hidden:
            return
        target.set_health(target.health - 50)
