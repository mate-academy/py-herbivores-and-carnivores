class Animal:
    alive = []
    health = 100
    hidden = False

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.alive.append(self)
        self.health = health

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")
