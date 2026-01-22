from __future__ import annotations


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

    @classmethod
    def kill(cls, animal: Herbivore) -> None:
        cls.alive.remove(animal)

    def __repr__(self) -> str:
        name, health, hidden = self.name, self.health, self.hidden
        return "{" + f"Name: {name}, Health: {health}, Hidden: {hidden}" + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        is_hidden = herbivore.hidden
        is_herbivore = isinstance(herbivore, Herbivore)
        is_alive = herbivore.health > 0
        can_bite = not is_hidden and is_herbivore and is_alive
        bite_damage = 50

        if can_bite:
            if herbivore.health <= bite_damage:
                # can be called from self.__class__.kill if bite not static
                Animal.kill(herbivore)
            herbivore.health -= bite_damage
