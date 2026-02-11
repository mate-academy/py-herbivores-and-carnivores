from app.animal import Animal
from app.carnivore import Carnivore
from app.herbivore import Herbivore


if __name__ == "__main__":
    # 1. Створюємо тварин
    lion = Carnivore("Simba")
    rabbit = Herbivore("Susan")

    print(f"Живих тварин: {len(Animal.alive)}")
    # Має бути 2

    # 2. Перший кусь
    lion.bite(rabbit)
    print(f"Здоров'я кролика після першого укусу: {rabbit.health}")
    # Має бути 50

    # 3. Кролик ховається
    rabbit.hide()
    print(f"Чи сховався кролик? {rabbit.hidden}")
    # Має бути True

    # 4. Спроба вкусити схованого кролика
    lion.bite(rabbit)
    print(f"Здоров'я після спроби нападу на схованого: {rabbit.health}")
    # Має залишитися 50

    # 5. Кролик виходить зі схованки і... фінал
    rabbit.hide()
    lion.bite(rabbit)

    print(f"Здоров'я кролика в кінці: {rabbit.health}")
    # Має бути 0
    print(f"Список живих в кінці: {Animal.alive}")
    # Має залишитися тільки Simba: [{Name: Simba, Health: 100, Hidden: False}]
