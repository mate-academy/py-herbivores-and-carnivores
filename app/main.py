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

    def check_health(self) -> bool:
        return self.health <= 0

    def remove_from_alive(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(obj: Herbivore) -> None:
        if isinstance(obj, Herbivore) and not obj.hidden:
            obj.health -= 50
            if obj.check_health():
                obj.remove_from_alive()
