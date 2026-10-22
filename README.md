# Травоїдні та хижі тварини

Перед початком ознайомтеся з [рекомендаціями](https://github.com/mate-academy/py-task-guideline/blob/main/README.md).


Природа добре підходить для відображення принципів об'єктно-орієнтованого програмування.
Усі екземпляри класу `Animal` повинні мати атрибути health, name і hidden.
За замовчуванням health дорівнює 100, а hidden — false.

Усі живі тварини повинні зберігатися в атрибуті класу `Animal.alive`.
Якщо здоров'я тварини досягає 0, тварина помирає, і її потрібно
видалити з `Animal.alive`.
```python
lion = Carnivore("Simba")
len(Animal.alive) == 1
isinstance(Animal.alive[0], Carnivore) is True
```

Створіть клас `Herbivore`. Цей клас повинен успадковуватися від `Animal`.
Клас Herbivore має метод `hide`, який змінює
властивість hidden тварини на протилежне значення та допомагає ховатися
від хижаків.
```python
rabbit = Herbivore("Susan")
rabbit.hide()
rabbit.hidden is True  
```

Створіть клас `Сarnivore`. Цей клас повинен успадковуватися від `Animal`.
Клас Carnivore має метод `bite`, який приймає
об'єкт травоїдної тварини та зменшує його health на 50. Метод
не працює, якщо переданий об'єкт є іншим хижаком або травоїдна тварина наразі ховається.
```python
lion = Carnivore("Lion King")
rabbit = Herbivore("Susan")
rabbit.health == 100
lion.bite(rabbit)
rabbit.health == 50  # укушено

rabbit.hide()
lion.bite(rabbit)
rabbit.health == 50  # лев не може вкусити захованого кролика

rabbit.hide()
lion.bite(rabbit)
rabbit.health == 0  # кролик помер

rabbit in Animal.alive  # False
# у Animal.alive немає мертвих тварин
```
Також реалізуйте можливість, щоб під час виведення `Animal.alive`
результат мав такий вигляд:
```python
pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)
# [{Name: Bagira, Health: 100, Hidden: False}, {Name: Kaa, Health: 100, Hidden: False}]
```
Підказка: використайте магічний метод.

### Примітка: перед надсиланням розв'язання перевірте свій код за допомогою цього [чекліста](checklist.md).
