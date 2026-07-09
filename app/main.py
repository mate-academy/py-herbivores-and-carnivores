class AnimalList(list):
    def __repr__(self) -> str:
        return f"[{', '.join(repr(animal) for animal in self)}]"


class Animal:
    alive: list["Animal"] = AnimalList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @staticmethod
    def get_alive_animals() -> list["Animal"]:
        return Animal.alive


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: "Animal") -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50

            if target.health <= 0:
                if target in Animal.alive:
                    Animal.alive.remove(target)
