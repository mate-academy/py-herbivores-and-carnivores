class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}"
                f", Health: {self.health}"
                f", Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        # 1. Перевірка: не можна кусати іншого хижака (Carnivore)
        if isinstance(target, Carnivore):
            print(f"{self.name} не може кусати іншого хижака!")
            return

        # 2. Перевірка: не можна кусати, якщо тварина сховалася
        if target.hidden:
            print(f"{self.name} не може знайти {target.name}"
                  f", бо той сховався!")
            return

        # Якщо все добре - кусаємо
        target.health -= 50

        # Логіка смерті: якщо здоров'я <= 0, видаляємо зі списку
        if target.health <= 0:
            if target in Animal.alive:
                Animal.alive.remove(target)
