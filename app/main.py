if __name__ == "__main__":
    from animals import Animal, Carnivore, Herbivore
else:
    from .animals import Animal, Carnivore, Herbivore


# Control check
if __name__ == "__main__":
    rabbit = Herbivore("Susan")
    pantera = Carnivore("Bagira")
    snake = Carnivore("Kaa")
    print(Animal.alive)
