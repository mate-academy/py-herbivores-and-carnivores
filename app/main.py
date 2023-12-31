class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)
    
    def __repr__(self) -> str:
        return (
            "{"
            f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}"
            "}"
            )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: Animal) -> None:
        if not victim.hidden and not isinstance(victim, Carnivore):
            victim.health -= 50

        if victim.health <= 0:
            Animal.alive = [
                animal for animal in Animal.alive if animal.name != victim.name
            ]
