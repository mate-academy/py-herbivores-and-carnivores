class Animal:

    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}"
                f"}}")

    def remove_dead_animal(self) -> None:
        for animal in Animal.alive:
            if animal.health <= 0:
                Animal.alive.remove(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: str) -> None:
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
            if victim.health <= 0:
                Animal.alive.remove(victim)
