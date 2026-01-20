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

    @classmethod
    def cleanup_dead_animals(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    def hide(self) -> None:
        self.hidden = not self.hidden

    def __str__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def __repr__(self) -> str:
        return str(self)


class Herbivore(Animal):

    def hide(self) -> None:
        super().hide()


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.hidden = True
                if herbivore in Animal.alive:
                    Animal.alive.remove(herbivore)
