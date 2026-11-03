from typing import List


class Animal:
    # Atributo de clase para almacenar todos los animales vivos
    alive: List["Animal"] = []

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
        # Aseguramos que la salud no baje de 0
        self._health = max(0, value)
        # Si la salud llega a 0, el animal muere y se elimina de Animal.alive
        if self._health == 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        # Método mágico para dar formato al representar o imprimir los objetos
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        # Cambia la propiedad hidden a su valor opuesto
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Animal) -> None:
        # Solo puede morder si el objetivo es un Herbivore y no está escondido
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
