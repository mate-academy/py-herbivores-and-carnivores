class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{" \
               f"Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}" \
               f"}}"


class Herbivore(Animal):
    def hide(self) -> None:

        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if not target.hidden and isinstance(target, Herbivore):
            target.health -= 50

            if target.health <= 0:
                for animal in Animal.alive:
                    if animal.name == target.name:
                        Animal.alive.remove(target)
