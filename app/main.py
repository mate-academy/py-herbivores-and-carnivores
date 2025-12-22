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

    def __repr__(self) -> str:
        return f"{{" \
               f"Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}" \
               f"}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def check_health(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Herbivore) -> None:
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
            victim.check_health()
