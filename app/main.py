class Animal:

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)
        # Animal.alive.append(self.__dict__)
        print(Animal.alive, len(Animal.alive))

    # def __str__(self):
    #     res = []
    #     for _ in self.alive:
    #         res.append(self.__dict__)
    #     Animal.alive = res
    #     return Animal.alive


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, other: object):
        if other.hidden == False and type(other) != Carnivore:
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
        # for i in Animal.alive:
        #     if i["health"] <= 0:
        #         Animal.alive.remove(i)


pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
# print(Animal.alive)
