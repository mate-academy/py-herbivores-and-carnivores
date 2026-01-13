from app.anilmal.animal_base import Animal
from app.anilmal.herbivore import Herbivore
from app.anilmal.carnivore import Carnivore


rabbit = Herbivore("Susan")
rabbit.hide()
print(rabbit.hidden is True)

lion = Carnivore("Lion King")
rabbit = Herbivore("Susan")
print(rabbit.health)
lion.bite(rabbit)
print(rabbit.health)

rabbit.hide()
lion.bite(rabbit)
print(rabbit.health)

rabbit.hide()
lion.bite(rabbit)
print(rabbit.health)

print(rabbit in Animal.alive)

pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)
