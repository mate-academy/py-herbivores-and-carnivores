class Animal:
    alive = list()

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        object_items_str = ", ".join(
            (f"{k.capitalize()}: {v}" for k, v in vars(self).items())
        )
        return f"{{{object_items_str}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, victim: Herbivore) -> None:
        if (
                victim.health > 0
                and isinstance(victim, Herbivore)
                and not victim.hidden
        ):
            victim.health -= 50
            if victim.health <= 0:
                Animal.alive.remove(victim)
