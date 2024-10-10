from types import TracebackType


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __enter__(self) -> None:
        pass

    def __exit__(
            self,
            exc_type: type,
            exc_val: Exception,
            exc_tb: TracebackType
    ) -> None:
        if self in Animal.alive:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Herbivore):
            if not target.hidden:
                target.health -= 50
                if target.health <= 0:
                    Animal.alive.remove(target)
