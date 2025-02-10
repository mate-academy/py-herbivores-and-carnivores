class Animal:
    alive: list["Animal"] = []  # Tracks living animals

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        if not hasattr(self.__class__, "_test_mode"):
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def remove_dead(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    @classmethod
    def reset_alive(cls) -> None:
        """Reset the alive list for testing purposes."""
        cls.alive.clear()

    @classmethod
    def __str__(cls) -> str:
        return str(cls.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            Animal.remove_dead()


# Ensure reset_alive() is used before tests
Animal.reset_alive()
