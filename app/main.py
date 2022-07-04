class Animal:
    def __init__(self, name: str, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden

class Herbivore(Animal):
    def hide(self):
        return super().__init__(self.name, self.health, hidden=True)

class Сarnivore(Animal):
    def bite(self):
        return
