class Animal:
    alive = list()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return "{" + f"Name: {self.name}," \
                     f" Health: {self.health}, Hidden: {self.hidden}" + "}"
