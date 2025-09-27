from __future__ import annotations


class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def take_damage(self, amount: int) -> None:
        self.health = max(0, self.health - amount)
        if self.health == 0 and self.Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: "
                f"{self.health}, Hidden: {self.hidden}}}")
