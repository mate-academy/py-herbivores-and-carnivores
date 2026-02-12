class Animal:
    # Class attribute to track all instances
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        # Automatically add to the tracking list upon creation
        Animal.alive.append(self)

    def _check_death(self):
        """Internal helper to clean up Animal.alive if health drops to 0."""
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self):
      """Controls how the object looks inside a list like Animal.alive."""
        strtmp = f"{{Name: {self.name}, Health: {self.health}"
        strtmp += f", Hidden: {self.hidden}}}"
        return strtmp


class Herbivore(Animal):
    def hide(self):
        """Toggles the hidden state."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal):
        """
        Reduces target health by 50 if target is a visible Herbivore.
        """
        # Logic check: Must be Herbivore and not hidden
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            target._check_death()
