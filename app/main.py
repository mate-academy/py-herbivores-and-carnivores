class Animal:
    alive = []
    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)
    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"
    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            Animal.alive.remove(self)

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Carnivore) or prey.hidden:
            return
            
        prey.take_damage(50)

