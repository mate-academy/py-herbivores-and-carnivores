class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        name = self.name
        health = self.health
        hidden = self.hidden
        return f"{{Name: {name}, Health: {health}, Hidden: {hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        for number, one_anim in enumerate(Animal.alive):
            if one_anim.name == self.name and isinstance(one_anim, Herbivore):
                one_anim.hidden = False if one_anim.hidden else True
                Animal.alive[number] = one_anim


class Carnivore(Animal):

    def bite(self, herbivore: Animal) -> None:
        for number, one_a in enumerate(Animal.alive):
            if one_a.name == herbivore.name and isinstance(one_a, Herbivore):
                if not one_a.hidden:
                    one_a.health -= 50
                    if one_a.health == 50:
                        Animal.alive[number] = one_a
                    else:
                        Animal.alive.pop(number)
