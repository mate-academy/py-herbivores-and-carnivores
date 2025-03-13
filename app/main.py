class Animal:
    _instances = []
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def remove_dead(cls) -> None:
        cls.alive = [obj for obj in cls.alive if obj.health > 0]

    @classmethod
    def update_alive(cls) -> None:
        cls.alive = [obj for obj in cls._instances if obj.health > 0]

    @classmethod
    def clear_instances(cls) -> None:
        cls._instances.clear()
        cls.alive.clear()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: object) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            Animal.remove_dead()  # Usuwamy martwe zwierzęta
