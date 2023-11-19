lion = [
    {
        'Name': "Simba",
        'Health': 100,
        'Hidden': False
    },

    {
        'Name': "King Lion",
        'Health': 100,
        'Hidden':  False,
    }
]
rabbit = [
    {
        'Name': "Susan",
        'Health': 100,
        'Hidden': False
    }
]

pantera = [
    {
        'Name': "Bagire",
        'Health': 100,
        'Hidden': False
    }
]


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self):
        if self.health == 50:
            self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, rabbit):
        if rabbit.hidden:
            rabbit.health = 100
        else:
            rabbit.health -= 50
        if rabbit.health <= 0:
            Animal.alive.remove(rabbit)


