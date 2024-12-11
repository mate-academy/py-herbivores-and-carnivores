class Animal:
    alive = []  # Список всех живых животных

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def remove_dead(cls):
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    @classmethod
    def reset_alive(cls):  # Метод для сброса списка живых животных
        cls.alive = []


class Herbivore(Animal):
    def __init__(self, name, health=100):
        super().__init__(name, health)

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def __init__(self, name, health=100):
        super().__init__(name, health)

    def bite(self, prey):
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            if prey.health <= 0:
                prey.health = 0
                Animal.remove_dead()
