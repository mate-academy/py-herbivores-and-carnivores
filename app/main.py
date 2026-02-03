from app.animal import Animal
from app.carnivore import Carnivore
from app.herbivore import Herbivore


def main() -> None:
    rabbit = Herbivore("Susan")
    lion = Carnivore("Simba")

    print(Animal.alive)

    lion.bite(rabbit)
    rabbit.hide()
    lion.bite(rabbit)
    lion.bite(rabbit)

    print(rabbit.health)
    print(Animal.alive)
