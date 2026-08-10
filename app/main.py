from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, value)
        if self._health == 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __str__(self) -> str:
        return f"{{Name: {self.name}, Health: {self._health}, Hidden: {self.hidden}}}"

    def __repr__(self) -> str:
        # Списки в Python використовують __repr__ елементів при друку списку.
        # Тому ми дублюємо __str__ тут, щоб print(Animal.alive) виглядав правильно.
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        # Type hint тут Animal, щоб не обмежувати метод тільки травоїдними на етапі типізації,
        # але логіка все одно перевіряє isinstance(prey, Herbivore) згідно з умовами.
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
