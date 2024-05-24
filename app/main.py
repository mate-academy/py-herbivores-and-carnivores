class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    @staticmethod
    def bite(subject: Animal) -> None:
        if isinstance(subject, Herbivore):
            if not subject.hidden:
                subject.health -= 50
                if subject.health <= 0:
                    Animal.alive.remove(subject)
