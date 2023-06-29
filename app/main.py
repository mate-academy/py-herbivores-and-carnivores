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
        self.__animal_birth__()

    def __animal_birth__(self) -> None:
        self.alive.append(self)

    def __animal_dead__(self) -> None:
        self.alive.remove(self)

    def __repr__(self) -> str:
        return ("{" + f"Name: {self.name}, "
                f"Health: {str(self.health)}, "
                f"Hidden: {str(self.hidden)}" + "}")


class Carnivore(Animal):
    def bite(self, bite_animal: Animal) -> None:
        if bite_animal.__class__ != Carnivore:
            if not bite_animal.hidden:
                if bite_animal.health >= 50:
                    bite_animal.health = bite_animal.health - 50
                else:
                    bite_animal.health = 0
        if bite_animal.health == 0:
            bite_animal.__animal_dead__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
