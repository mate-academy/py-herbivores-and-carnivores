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
        return f"" \
               f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}" \
               f"}}"


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(target: Animal) -> None:
        if isinstance(target, Carnivore) or target.hidden:
            pass
        else:
            target.health -= 50
            if target.health <= 0:
                Animal.alive.remove(target)
