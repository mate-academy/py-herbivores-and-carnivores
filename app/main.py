class AnimalList(list):
    def __repr__(self) -> str:
        return "[" + ", ".join(repr(animal) for animal in self) + "]"


class Animal:
    alive = AnimalList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def _remove_if_dead(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not isinstance(
            herbivore, Carnivore
        ):
            if not herbivore.hidden:
                herbivore.health -= 50
                herbivore._remove_if_dead()
