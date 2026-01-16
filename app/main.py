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

    def get_damage(self, damage: int = 50) -> None:
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.die()

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def convert_to_dict(self) -> dict:
        return {
            "Name": self.name,
            "Health": self.health,
            "Hidden": self.hidden
        }

    def __repr__(self) -> str:
        return (
            f"\u007bName: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}\u007d"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Herbivore):
            if target.hidden:
                print(f"{self.name} cannot bite hidden {target.name}")
            else:
                target.get_damage(50)
