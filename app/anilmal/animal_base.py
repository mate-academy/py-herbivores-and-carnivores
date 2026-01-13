class Animal:
    alive = []
    animal = {}

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.animal[self.name] = self
        Animal.alive.append(self)

    def __repr__(self) -> None:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")
