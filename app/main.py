class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        substr = ""
        substr += f"{{Name: {self.name}, Health: {self.health}"
        substr += f", Hidden: {self.hidden}}}"
        return substr


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore_object: Herbivore) -> None:
        if (isinstance(herbivore_object, Herbivore)
                and herbivore_object.hidden is False):
            herbivore_object.health -= 50
            if herbivore_object.health <= 0:
                i = 0
                for animal in self.alive:
                    print(f"{animal.name} {herbivore_object.name}")
                    if animal.name == herbivore_object.name:
                        del self.alive[i]
                        break
                    i += 1
