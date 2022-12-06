class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return "{Name: %s, Health: %s, Hidden: %s}" \
               % (self.name, self.health, self.hidden)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if self.hidden is False else False


class Carnivore(Animal):
    def bite(self, herb_is_bite: Herbivore) -> Herbivore:
        if herb_is_bite.hidden is False and\
                isinstance(herb_is_bite, Herbivore):
            herb_is_bite.health -= 50
        if herb_is_bite.health <= 0:
            Animal.alive = [
                alive
                for alive in self.alive
                if alive is not herb_is_bite
            ]

        return herb_is_bite
