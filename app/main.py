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

        if health > 0:
            Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        text = "{{Name: {}, Health: {}, Hidden: {}}}"
        return text.format(self.name, self.health, self.hidden)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if target.hidden:
            return

        if isinstance(target, Carnivore):
            return

        target.health -= 50

        if target.health <= 0:
            target.health = 0
            target.die()
