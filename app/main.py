class Animal:
    alive: list["Animal"] = []

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

    def die(self) -> None:
        Animal.alive.remove(self)
        print(f"{self.name} is dead!")

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            herb: Herbivore
    ) -> None:
        if not isinstance(herb, Herbivore):
            return

        if herb.hidden:
            print(f"{self.name} cannot bite hidden {herb.name}")
            return

        herb.health -= 50
        print(f"{herb.name} is bited!")

        if herb.health <= 0:
            herb.die()
