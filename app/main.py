class Animal(object):
    alive = []

    def __init__(self, name: str, ) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(
            {"Name": self.name,
             "Health": self.health,
             "Hidden": self.hidden}
        )

    def __str__(self) -> str:
        return f"\nName = {self.name},\n" \
               f"Current hp = {self.health},\n" \
               f"Hiding? = {'yes' if self.hidden == True else 'no'}\n"


class Herbivore(Animal):

    def hide(self):
        self.hidden = True

    def __isub__(self, damage):
        self.health -= damage
        return self.health


class Carnivore(Animal):
    @staticmethod
    def bite(target: "Herbivore"):
        if isinstance(target, Herbivore) and target.hidden is False:
            target.__isub__(50)
        if target.health < 1:
            dead = 0
            for animal in Animal.alive:
                if animal.get("Name") == target.name:
                    Animal.alive.remove(Animal.alive[dead])
                else:
                    dead += 1
