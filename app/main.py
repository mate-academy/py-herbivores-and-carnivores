class Animal:
    alive = []  # Class attribute to track all alive animals

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)  # Add instance to alive list

    def __repr__(self) -> None:
        """Modify print output of Animal.alive"""
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"

    def die(self) -> None:
        """Remove dead animal from alive list"""
        if self in Animal.alive:
            Animal.alive.remove(self)

    @classmethod
    def __str__(cls) -> str:
        """String representation for Animal.alive"""
        return str(cls.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        """Toggle the hidden attribute"""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Herbivore) -> None:
        """Bite a herbivore and decrease its health"""
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            if prey.health <= 0:
                prey.die()
