class Animal:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive = True if self.health > 0 else False

class Herbivore(Animal):
    def hide(self):
        self.hidden = True

