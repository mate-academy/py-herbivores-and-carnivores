class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str = "",
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}"
                f"}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            target: Animal
    ) -> None:
        if isinstance(target, Carnivore):
            return
        if not target.hidden:
            target.health -= 50
            if target.health <= 0:
                Animal.alive.remove(target)
