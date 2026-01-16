class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def print_alive(cls) -> None:
        return [
            {
                "Name": animal.name,
                "Health": animal.health,
                "Hidden": animal.hidden
            } for animal in cls.alive
        ]


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, victim: Herbivore) -> bool:
        if isinstance(victim, Carnivore):
            print("Carnivore cannot bite by another carnivore!")
        elif not victim.hidden:
            victim.health -= 50
            if victim.health <= 0:
                victim.health = 0
                victim.die()
