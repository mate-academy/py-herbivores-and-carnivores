class Animal:
    # створюємо список для збереження обʼєктів
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)
        # перевіряємо чи не вмерла тварина, якщо здоровʼя <= 0
        self.update_status()

    def update_status(self) -> None:
        # Якщо здоров'я тварини досягає 0, видаляємо звіра з Animal.alive.
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        # використовуємо магію, щоб отримати бажаний вигляд даних по тваринам
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    """
    Травоїдний має метод hide, який змінює приховану властивість звіра
    на протилежне значення і допомагає сховатися від м'ясоїдних.
    """
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    """
    bite метод, бере травоїдний об’єкт і знижує здоров’я об’єкта на 50.
    Метод не працює, якщо це хижа тварина або травоїдна тварина ховається.
    """
    @staticmethod
    def bite(herbivore_animal: Herbivore) -> None:
        if not herbivore_animal.hidden and \
                isinstance(herbivore_animal, Herbivore):
            herbivore_animal.health -= 50
            # перевіряємо, чи не вмерла тварина
            herbivore_animal.update_status()
