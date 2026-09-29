from app.models import Animal, Carnivore, Herbivore

if __name__ == "__main__":
    pantera = Carnivore("Bagira")
    snake = Carnivore("Kaa")
    rabbit = Herbivore("Susan")
    print(Animal.alive)
