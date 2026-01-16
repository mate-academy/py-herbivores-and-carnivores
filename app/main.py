class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    @staticmethod
    def update_alive_status() -> None:
        Animal.alive = [
            animal for animal in Animal.alive if animal.health > 0
        ]

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True
        Animal.update_alive_status()


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore):
            if animal.hidden:
                print(f"{self.name} cannot bite hidden {animal.name}")
                return
            animal.health -= 50
            animal.update_alive_status()
