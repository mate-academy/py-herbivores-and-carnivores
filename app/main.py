class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )

    @classmethod
    def _update_alive(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            Animal._update_alive()

    def __str__(self) -> str:
        return f"{[animal for animal in self.alive]}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.take_damage(50)
