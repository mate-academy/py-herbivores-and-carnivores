class Animal (object):

    alive = list["Animal"] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def _check_death(self):
        if not self.alive() and self in Animal.alive:
            Animal.alive.remove(self)
            
    def is_alive(self):
        return self.health > 0
        
    def __repr__(self) -> str:
        return (
            f"Name: {self.name} Health: {self.health}"
            f"Hidden: {self.hidden}"
        )


class Herbivore (Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore (Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if herbivore.hidden:
            return

        if not isinstance(herbivore, Herbivore):
            return
        
        if not herbivore.is_alive():
            return

        herbivore.health -= 50
        herbivore._check_death()
