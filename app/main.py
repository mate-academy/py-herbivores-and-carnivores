class AliveList(list):
    def __repr__(self) -> str:
        formatted_animals = [
            {
                "Name": animal.name,
                "Health": animal.health,
                "Hidden": animal.hidden
            }
            for animal in self
        ]
        return str(formatted_animals).replace("'", "")


class Animal:
    alive = AliveList()

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self._health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, value)
        if self._health == 0:
            self._die()

    def _die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
        print(f"{self.name} now is"
              f"{"hidden" if self.hidden else "no hidden"}.")


class Carnivore(Animal):
    def bite(self, target: str) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            damage = 50
            target.health -= damage
            print(f"{self.name} bite {target.name}!"
                  f"Health {target.name}: {target.health}")
        elif isinstance(target, Carnivore):
            print(f"{self.name} can't bite other carnivore.")
        elif target.hidden:
            print(f"{self.name} can't bite {target.name}, because it hidden.")
        else:
            print(f"{self.name} don't bite the target.")
