class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def __repr__(self) -> str:
        class_dict = {
            "Name": self.name,
            "Health": self.health,
            "Hidden": self.hidden
        }
        rep = (f"{{"
               f"Name: {class_dict["Name"]}, "
               f"Health: {class_dict["Health"]}, "
               f"Hidden: {class_dict["Hidden"]}"
               f"}}")
        return rep


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, whom: Herbivore) -> None:
        if (not whom.hidden) and isinstance(whom, Herbivore):
            whom.health -= 50

        if whom.health <= 0:
            Animal.alive.remove(whom)
