class Animal:
    alive = []

    def __init__(self, name: str,
               health: int = 100,
               hidden: bool = False
               ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)
    
    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: "
                f"{self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self):
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self,
             prey: object
             ) -> None:
        if prey.hidden:
            pass
        else:
            prey.hp -= 50
            if prey.hp <= 0:
                prey.die
