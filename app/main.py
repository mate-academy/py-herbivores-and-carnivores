class Animal:
    alive = []  # Список всех живых животных

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @staticmethod
    def remove_dead():
        Animal.alive = [animal for animal in Animal.alive if animal.health > 0]


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore):
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            Animal.remove_dead()