class Animal:
    alive = []

    def __init__(self, name, health=100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden

    def take_damage(self):
        if self.hidden:
            pass
        else:
            if self.health <= 50:
                self.alive.remove(self)
            else:
                self.health -= 50


class Carnivore(Animal):
    def bite(self, victim: Animal):
        if isinstance(victim, Carnivore):
            pass
        if isinstance(victim, Herbivore):
            victim.take_damage()
