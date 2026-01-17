class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        if not Animal.alive:
            return "No animals are alive 🐾"
        return (f"{{"
                f"Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @classmethod
    def bite(
            cls,
            target: Herbivore) -> None:
        if isinstance(target, cls) or target.hidden is True:
            pass
        else:
            target.health -= 50
            if target.health <= 0:
                Animal.alive.remove(target)
