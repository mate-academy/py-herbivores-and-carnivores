class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def remove_from_alive(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        result = {
            i.capitalize(): getattr(self, i)
            for i in vars(self)
            if not i.startswith("_")
        }
        return str(result).replace("'", "")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, victim: Herbivore) -> None:
        if isinstance(victim, Carnivore):
            return
        if victim.hidden is True:
            return
        else:
            victim.health -= 50
            victim.remove_from_alive()
