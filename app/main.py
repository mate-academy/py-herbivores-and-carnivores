class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def check_health(self) -> None:
        if self.health <= 0:
            print(f"{self.name} is dead.")
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
        status = "hidden" if self.hidden else "visible"
        print(f"{self.name} now {status}.")


class Carnivore(Animal):

    def bite(self, target: Herbivore) -> None:
        if not isinstance(target, Herbivore):
            print(f"{self.name} cannot bite "
                  f"{target.name}: target is not a Herbivore.")
            return

        if target.hidden:
            print(f"{self.name} cannot bite {target.name}: hidden.")
            return

        print(f"{self.name} bite {target.name} (-50 health).")
        target.health -= 50
        target.check_health()
