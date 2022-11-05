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

    @classmethod
    def is_alive(cls) -> None:
        for animal in cls.alive:
            if animal.health <= 0:
                cls.alive.remove(animal)

    def __repr__(self) -> str:
        animal_list = "{Name: %s, Health: %s, Hidden: %s}" \
                      % (self.name, self.health, self.hidden)
        return str(animal_list)


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(animal: object) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            Animal.is_alive()
