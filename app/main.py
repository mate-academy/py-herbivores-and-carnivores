class Animal():
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:

        parts = [
            f"Name: {self.name}",
            f"Health: {self.health}",
            f"Hidden: {self.hidden}"
        ]
        return "{" + ", ".join(parts) + "}"

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            Animal.alive.remove(self)
            # return f"{self.name} is dead"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):

    def bite(self, animal_obj: Animal) -> None:
        if not isinstance(animal_obj, Herbivore):
            return
        elif animal_obj.hidden:
            return
        elif isinstance(animal_obj, Herbivore):
            animal_obj.take_damage(50)
