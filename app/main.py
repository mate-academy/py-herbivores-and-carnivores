
class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    
    def damage_taker(self, amount: int) -> None:
        self.health -= amount

        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal) :

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: "Animal") -> None:
        if not isinstance(other, Herbivore) or other.hidden == True:
            return
        other.damage_taker(50)
