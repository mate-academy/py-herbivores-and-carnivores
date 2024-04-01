class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.die()

    def die(self) -> None:
        Animal.alive.remove(self)
        print(f"{self.name} has died.")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Carnivore) or target.hidden:
            print("Cannot bite!")
            return
        target.health -= 50
        if target.health <= 0:
            target.health = 0
            target.die()
