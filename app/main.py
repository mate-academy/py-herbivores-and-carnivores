from typing import List, ClassVar


class Animal:
    alive: ClassVar[List["Animal"]] = []  # Список всех живых животных

    def __init__(self, name: str, health: int = 100):
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def remove_dead(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    @classmethod
    def reset_alive(cls) -> None:
        cls.alive = []

    @classmethod
    def __str__(cls) -> str:
        return str([repr(animal) for animal in cls.alive])


class Herbivore(Animal):
    def __init__(self, name: str, health: int = 100):
        super().__init__(name, health)

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def __init__(self, name: str, health: int = 100):
        super().__init__(name, health)

    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            if prey.health <= 0:  # Проверяем здоровье жертвы
                prey.health = 0
                Animal.remove_dead()  # Убираем мёртвое животное из списка


# Пример использования
if __name__ == "__main__":
    Animal.reset_alive()
    lion = Carnivore("Simba")
    rabbit = Herbivore("Susan", 100)

    print(f"До укуса: {rabbit.health}, скрыт: {rabbit.hidden}")
    lion.bite(rabbit)
    print(f"После укуса: {rabbit.health}, скрыт: {rabbit.hidden}")

    rabbit.hide()
    lion.bite(rabbit)
    print(f"Попытка укусить скрытого кролика: {rabbit.health}")

    rabbit.hide()
    lion.bite(rabbit)
    print(f"После повторного укуса: {rabbit.health}")
    print(f"Живые животные: {Animal.alive}")