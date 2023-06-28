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
        self.animal_birth(self)

    @classmethod
    def animal_birth(cls, birth_animal: "Animal") -> None:
        cls.alive.append(birth_animal)

    @classmethod
    def animal_dead(cls, dead_animal: "Animal") -> None:
        alive_index = cls.alive.index(dead_animal)
        cls.alive.pop(alive_index)

    def __repr__(self) -> str:
        return ("{" + f"Name: {self.name}, "
                f"Health: {str(self.health)}, "
                f"Hidden: {str(self.hidden)}" + "}")


class Carnivore(Animal):
    @classmethod
    def bite(cls, bite_animal: Animal) -> None:
        if bite_animal.__class__ != Carnivore:
            if bite_animal.health != 0:
                if not bite_animal.hidden:
                    if bite_animal.health >= 50:
                        bite_animal.health = bite_animal.health - 50
                    else:
                        bite_animal.health = 0
                    if bite_animal.health == 0:
                        cls.animal_dead(bite_animal)


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False
