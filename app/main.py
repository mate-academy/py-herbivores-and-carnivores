lion = [
    {
        "Name": "Simba",
        "Health": 100,
        "Hidden": False
    },

    {
        "Name": "King Lion",
        "Health": 100,
        "Hidden": False,
    }
]
rabbit = [
    {
        "Name": "Susan",
        "Health": 100,
        "Hidden": False
    }
]

pantera = [
    {
        "Name": "Bagire",
        "Health": 100,
        "Hidden": False
    }
]


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{" \
               f"Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}" \
               f"}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, rabbit: Herbivore) -> None:
        if isinstance(rabbit, Carnivore) or rabbit.hidden:
            return
        rabbit.health -= 50
        if rabbit.health <= 0:
            Animal.alive.remove(rabbit)
