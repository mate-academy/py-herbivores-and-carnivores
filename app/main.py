class Animal:
    alive = []

    def __init__(
        self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: "
            f"{str(self.health)}, "
            f"Hidden: {str(self.hidden)}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        elif self.hidden is True:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, victim: Animal) -> None:
        if victim.hidden is False and isinstance(victim, Herbivore):
            victim.health -= 50
            if victim.health <= 0:
                Animal.alive.remove(victim)
