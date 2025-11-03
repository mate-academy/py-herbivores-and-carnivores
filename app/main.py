class Animal:
    alive = []  # lista com todos os animais vivos

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def die(self):
        """Remove o animal da lista se morrer."""
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self):
        """Representação personalizada para print(Animal.alive)."""
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        """Alterna o estado hidden (se esconder ou aparecer)."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target):
        """Morde um herbívoro e reduz sua saúde em 50."""
        if not isinstance(target, Herbivore):
            return  # não morde carnívoros
        if target.hidden:
            return  # não pode morder herbívoro escondido

        target.health -= 50
        if target.health <= 0:
            target.health = 0
            target.die()
