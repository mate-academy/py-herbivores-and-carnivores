class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        # Додаємо екземпляр до класової змінної
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):

    def bite(self, ani: "Animal") -> None:
        if isinstance(ani, Herbivore) and not ani.hidden and ani.health > 0:
            ani.health -= 50
            if ani.health <= 0:
                ani.die()
