from app.animals.carnivore import Carnivore
from app.animals.herbivore import Herbivore
from app.animals.base.animal import Animal


if __name__ == "__main__":
    lion = Carnivore("Lion King")
    rabbit = Herbivore("Susan")
    assert rabbit.health == 100
    lion.bite(rabbit)
    assert rabbit.health == 50

    rabbit.hide()
    lion.bite(rabbit)
    assert rabbit.health == 50

    print(rabbit)

    rabbit.hide()
    lion.bite(rabbit)
    assert rabbit.health == 0

    assert rabbit not in Animal.alive
