# flake8: noqa: E501


class Animal:
    # Class attribute to track all instances
    alive: list["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name = name
        if(health <=0):
            self.health = 0
        else:
            self.health = health
        self.hidden = hidden
        # Automatically add to the tracking list upon creation
        Animal.alive.append(self)        

    def _check_death(self) -> None:
        """Internal helper to clean up Animal.alive if health drops to 0."""
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        """Controls how the object looks inside a list like Animal.alive."""
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        """
        Reduces target health by 50 if target is a visible Herbivore.
        """
        # Logic check: Must be Herbivore and not hidden
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            target._check_death()
