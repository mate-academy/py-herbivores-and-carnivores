from app.animal import Animal, Carnivore, Herbivore


if __name__ == "__main__":
    lion = Carnivore("Simba")
    print(len(Animal.alive) == 1)
    print(isinstance(Animal.alive[0], Carnivore) is True)

    rabbit = Herbivore("Susan")
    rabbit.hide()
    print(rabbit.hidden is True)

    lion = Carnivore("Lion King")
    rabbit = Herbivore("Susan")
    print(rabbit.health == 100)
    lion.bite(rabbit)
    print(rabbit.health == 50)  # bited

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health == 50)  # lion cannot bite hidden rabbit

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health == 0)  # rabbit is dead

    print(rabbit in Animal.alive)  # False
    # there is no dead animals in Animal.alive

    pantera = Carnivore("Bagira")
    snake = Carnivore("Kaa")
    print(Animal.alive)
