class Animal:

    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{{Name: {}, Health: {}, Hidden: {}}}".\
            format(self.name, self.health, self.hidden)

    @staticmethod
    def is_dead(lunch_name: str) -> None:
        if lunch_name.health <= 0:
            Animal.alive.pop()


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, lunch_name: str) -> None:
        if isinstance(lunch_name, Herbivore) and lunch_name.hidden is False:
            lunch_name.health -= 50
            self.is_dead(lunch_name)
