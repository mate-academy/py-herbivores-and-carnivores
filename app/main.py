class Animal:
    alive = []  # Класс-атрибут для хранения всех живых животных

    def __init__(self, name: str, health: int = 100) -> None:
        """
        Инициализирует животное с именем, здоровьем и скрытностью.
        """
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        """
        Возвращает строковое представление животного.
        """
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        """
        Удаляет животное из списка живых, если здоровье равно или меньше 0.
        """
        if self in Animal.alive:
            Animal.alive.remove(self)

    def check_health(self) -> None:
        """
        Проверяет здоровье животного и убирает из списка живых
        при его отсутствии.
        """
        if self.health <= 0:
            self.die()


class Herbivore(Animal):
    def hide(self) -> None:
        """
        Меняет состояние скрытности травоядного.
        """
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        """
        Уменьшает здоровье травоядного на 50, если оно не скрыто.
        """
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            herbivore.check_health()
