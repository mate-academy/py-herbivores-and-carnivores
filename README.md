# Herbivores and carnivores

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.


Nature is well suited to reflect the principles of Object Oriented Programming. 
All instances of the `Animal` class must have health, name and hidden attribute. 
Health is 100 and hidden is false by default.

All alive animals should be in the `__class__` attribute `Animal.alive`. 
If the health of the animal reaches 0, the beast dies and it should 
be removed from `Animal.alive`.
```python
lion = Carnivore("Simba")
len(Animal.alive) == 1
isinstance(Animal.alive[0], Carnivore) is True
```

Create a `Herbivore` class. This class should inherit from Animal. 
Herbivore has a method of `hide`, which changes 
the hidden property of the beast to the opposite value and helps to hide 
from carnivores.
```python
rabbit = Herbivore("Susan")
rabbit.hide()
rabbit.hidden is True  
```

Create a `Сarnivore` class. This class should inherit from Animal. 
Carnivore has a `bite` method, which takes a 
herbivore object and decreases the object's health by 50. The method 
does not work if it is another сarnivore, or the herbivore is currently hiding.
```python
lion = Carnivore("Lion King")
rabbit = Herbivore("Susan")
rabbit.health == 100
lion.bite(rabbit)
rabbit.health == 50  # bited

rabbit.hide()
lion.bite(rabbit)
rabbit.health == 50  # lion cannot bite hidden rabbit

rabbit.hide()
lion.bite(rabbit)
rabbit.health == 0  # rabbit is dead

rabbit in Animal.alive  # False
# there is no dead animals in Animal.alive
```
Also implement feature that when you print `Animal.alive` it
should look like this:
```python
pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)
# [{Name: Bagira, Health: 100, Hidden: False}, {Name: Kaa, Health: 100, Hidden: False}]
```
Hint: Use magic method.

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
