class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def check_health(self):
        if self.health <= 0:
            self.remove_dead_from_alive()

    def remove_dead_from_alive(self):
        Animal.alive.remove(self)

    def __repr__(self):
        return "{Name: %s, Health: %s, Hidden: %s}" \
               % (self.name, self.health, self.hidden)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore):
        if isinstance(herbivore, Herbivore) \
                and not herbivore.hidden:
            herbivore.health -= 50
            herbivore.check_health()
