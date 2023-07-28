class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def take_damage(self, damage: int) -> None:
        if not self.hidden:
            self.health = max(self.health - damage, 0)
            if self.health <= 0:
                self.die()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Herbivore, hide: int = 50) -> None:
        if not self.hidden and isinstance(target, Herbivore) and not target.hidden:
            target.take_damage(hide)
