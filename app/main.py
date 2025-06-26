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


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden

    def loose_hp(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            Animal.alive.remove(self)


class Carnivore(Animal):

    @staticmethod
    def bite(victim: str) -> None:
        if not isinstance(victim, Herbivore) or victim.hidden:
            return
        victim.loose_hp(50)
