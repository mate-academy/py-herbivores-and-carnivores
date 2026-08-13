class Animal:
    alive = []

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

    def dict_with_info(self) -> dict:
        return {
            "Name": self.name,
            "Health": self.health,
            "Hidden": self.hidden,
        }

    def __repr__(self) -> str:
        info = self.dict_with_info()
        formatted = ", ".join(f"{key}: {value}" for key, value in info.items())
        return f"{{{formatted}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if (
                isinstance(other, Herbivore)
                and not other.hidden
                and other in Animal.alive
        ):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
