class AliveList(list):
    def __repr__(self) -> str:
        animals = []

        for animal in self:
            animals.append(
                f"{{Name: {animal.name}, "
                f"Health: {animal.health}, "
                f"Hidden: {animal.hidden}}}"
            )

        return "[" + ", ".join(animals) + "]"


class Animal:
    alive = AliveList()

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def take_damage(self, damage: int) -> None:
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def animal_alive(cls) -> None:
        animals_alive = []

        for animal in cls.alive:
            one_animal = {
                "Name": animal.name,
                "Health": animal.health,
                "Hidden": animal.hidden,
            }
            animals_alive.append(one_animal)

        print(animals_alive)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.take_damage(50)
