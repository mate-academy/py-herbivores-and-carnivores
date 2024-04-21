class Animal:
    alive = []

    def __init__(self, n: str, h: int = 100, hid: bool = False) -> None:
        self.n = n
        self.h = h
        self.d = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        res = f"{{Name: {self.n: str}, Health: {self.h: int}, Hidden: {self.d: bool}}}"
        return res


class Herbivore(Animal):
    def hide(self) -> bool:
        if self.d:
            self.d = False
        else:
            self.d = True


class Carnivore(Animal):
    def bite(self, animal: object) -> object:
        if isinstance(animal, Herbivore) and not animal.d:
            animal.h -= 50
            if animal.h <= 0:
                Animal.alive.remove(animal)
