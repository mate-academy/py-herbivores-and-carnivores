class Animal:
    alive: bool = True
    
    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False,
    ) -> None:
        self.name = name
        self._health = health
        self.hidden = hidden
        Animal.alive.append(self)

def __str__(self):
        status = "Hidden" if self.hidden else "Visible"
        return f"{self.name} | Health: {self.health} | Status: {status}"




    
    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(
        self,
        value: int,
    ) -> None:
        self._health = max(value, 0)
        if self._health == 0 and self in Animal.alive:
            Animal.alive.remove(self)

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        prey: Animal,
    ) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            if prey.health <= 0:
                prey.health = 0
                if prey in Animal.alive:
                    Animal.alive.remove(prey)