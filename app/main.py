from __future__ import annotations


class Animal:
    # Список усіх живих тварин.
    # Це атрибут класу, тому він спільний для всіх об'єктів. добавь анотации
    alive: list[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False  # За замовчуванням тварина не ховається
        Animal.alive.append(self)  # Додаємо створену тварину до списку живих

    def take_damage(self, damage: int) -> None:
        """
        Зменшує здоров'я тварини.
        Якщо здоров'я стало 0 або менше —
        тварина помирає.
        """

        self.health -= damage

        # Не дозволяємо здоров'ю бути від'ємним
        if self.health <= 0:
            self.health = 0

            # Якщо тварина ще є у списку живих —
            # видаляємо її.
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        """
        Викликається при друкуванні об'єкта
        або списку об'єктів.
        """

        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    """
    Травоїдна тварина.
    """

    def hide(self) -> None:
        """
        Міняє стан приховування.

        False -> True
        True -> False
        """

        self.hidden = not self.hidden


class Carnivore(Animal):
    """
    Хижак.
    """

    def bite(self, animal: Herbivore) -> None:
        """
        Кусає лише травоїдних,
        які не сховалися.
        """

        # Якщо це не Herbivore —
        # нічого не робимо.
        if not isinstance(animal, Herbivore):
            return

        # Якщо тварина сховалася —
        # вкусити не можна.
        if animal.hidden:
            return

        # Наносимо шкоду.
        animal.take_damage(50)
