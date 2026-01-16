# Створюємо базовий клас Animal
class Animal:
    # Статичний атрибут для зберігання всіх живих тварин.
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        """
        Ініціалізуємо об'єкт тварини.
        :param name: Ім'я тварини.
        """
        self.name = name  # Ім'я тварини.
        # Здоров'я за замовчуванням дорівнює 100.
        self.health = health
        # Атрибут "hidden" за замовчуванням дорівнює False.
        self.hidden = False
        # Додаємо тварину до списку "alive".
        Animal.alive.append(self)

    def __repr__(self) -> str:
        """
        Магічний метод для відображення списку живих тварин.
        """
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def check_death(self) -> None:
        """
        Перевіряємо, чи здорова тварина.
        Якщо здоров'я = 0, то видаляємо її з Animal.alive.
        """
        if self.health <= 0:
            Animal.alive.remove(self)


# Створюємо клас Herbivore, який наслідується від Animal.
class Herbivore(Animal):
    def hide(self) -> None:
        """
        Метод для зміни статусу "hidden".
        Використовується для того, щоб травоїдні ховалися.
        """
        self.hidden = not self.hidden  # Перемикаємо значення між True і False.


# Створюємо клас Carnivore, який наслідується від Animal.
class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        """
        Метод "bite" дозволяє хижакові нападати на травоїдну тварину.
        :param herbivore: Об'єкт травоїдної тварини, на яку нападає хижак.
        """
        # Перевіряємо, чи травоїдна тварина не ховається та чи це не хижак.
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            # Зменшуємо здоров'я травоїдної на 50 одиниць.
            herbivore.health -= 50
            # Перевіряємо, чи травоїдна тварина ще жива.
            herbivore.check_death()
