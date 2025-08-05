class AliveList(list):

    def __repr__(self) -> str:
        alive_list = []
        for animal in self:
            animal_dict = {"Name": animal.name, "Health": animal.health,
                           "Hidden": animal.hidden}
            alive_list.append(animal_dict)
        return f"{alive_list}"


class Animal:
    alive = AliveList()

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
            if animal.health <= 0:
                animal.alive.remove(animal)
