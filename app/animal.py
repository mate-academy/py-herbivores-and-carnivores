class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def get_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.already_died()

    def already_died(self) -> None:
        Animal.alive.remove(self)

    def __str__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, Hidden: {self.hidden}}}"
