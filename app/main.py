class Animal:
    # список усіх живих тварин
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        # перемикаємо стан схованки
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        # хижак не кусає іншого хижака або сховану жертву
        if not isinstance(herbivore, Herbivore) or herbivore.hidden:
            return

        herbivore.health -= 50

        # якщо здоров'я скінчилось, прибираємо зі списку живих
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
