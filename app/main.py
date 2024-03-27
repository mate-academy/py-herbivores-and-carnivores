from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def remove_alive(cls, inst: Herbivore | Carnivore) -> None:
        if inst in cls.alive:
            cls.alive.remove(inst)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, inst: Carnivore | Herbivore) -> None:
        if isinstance(inst, Carnivore) or inst.hidden:
            print_hidden = "hidden" if isinstance(inst, Herbivore) else ""
            print(f"{self.name} cannot bite {print_hidden} {inst.name}")
        else:
            inst.health -= 50

        if inst.health <= 0:
            Animal.remove_alive(inst)
