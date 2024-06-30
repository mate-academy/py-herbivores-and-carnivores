class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def hide(self) -> None:
        self.hidden = not self.hidden

    def is_alive(self) -> bool:
        return self.health > 0

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return "{{Name: {}, Health: {}, Hidden: {}}}".format(
            self.name,
            self.health,
            self.hidden)

    @classmethod
    def update_alive(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.is_alive()]

    @classmethod
    def __str__(cls) -> str:
        return str(cls.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        super().hide()


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                animal.die()
        Animal.update_alive()
