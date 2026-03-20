class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other):
        # Проверка: кусаем только травоядных и не скрытых
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return

        other.health -= 50

        if other.health <= 0:
            other.health = 0
            other.die()
