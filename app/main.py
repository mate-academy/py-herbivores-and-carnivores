class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}"
                f", Health: {self.health}, Hidden: {self.hidden}}}")

    @classmethod
    def __str__(cls) -> str:
        return str(cls.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
        state = "hidden" if self.hidden else "visible"
        print(f"Herbivore is now {state}")


class Carnivore(Animal):
    def bite(self, victim: Animal) -> None:
        if isinstance(victim, Herbivore):
            if not victim.hidden:
                victim.health -= 50
                print(f"{self.name} bit {victim.name}"
                      f". {victim.name} now has {victim.health} health.")
            else:
                print(f"{self.name}"
                      f" couldn't bite {victim.name} because it's hidden.")

            if victim.health <= 0:
                Animal.alive.remove(victim)
                print(f"{victim.name} has died.")
        else:
            print(f"{self.name}"
                  f" can't bite {victim.name} because it is not a Herbivore.")
