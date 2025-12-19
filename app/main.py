alive = []

class Animal:
    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.hidden = hidden
        self.health = health
        alive.append(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = True

class Carnivore(Animal):
    def bite(self, victim: Herbivore):
        if isinstance(victim, Carnivore):
            return
        if victim.hidden:
            return
        else:
            victim.health -= 50
            if victim.health <= 0:
                alive.remove(victim)


        