class Animal:
    alive = []

    def __init__(self, name: str,  health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @classmethod
    def get_alive(cls):
        result = []
        for animal in cls.__dict__['alive']:  
            animal_dict = {
                "Name": animal.name,
                "Health": getattr(animal, 'health', 100), 
                "Hidden": getattr(animal, 'hidden', False) 
            }
            result.append(animal_dict)
        return result

class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):

    def bite(self, herbivore: Herbivore):
        if not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)

if __name__ == "__main__":
    lion = Carnivore("Simba")
    print(f"Number of alive animals: {len(Animal.alive) == 1}")
    print(f"Is first alive animal a Carnivore? {isinstance(Animal.alive[0], Carnivore)}")
    lion = Carnivore("Lion King")
    rabbit = Herbivore("Susan")
    print(f"Is Rabbit's health 100? {rabbit.health == 100}")
    lion.bite(rabbit)
    print(f"Rabbit's health after bite: {rabbit.health}")  # bited

    rabbit.hide()
    lion.bite(rabbit)
    print(f"Rabbit's health after hiding and bite: {rabbit.health}")  # lion cannot bite hidden rabbit

    rabbit.hide()
    lion.bite(rabbit)
    print(f"Rabbit's health after second hiding and bite: {rabbit.health}")  # rabbit is dead

    print(f" Is rabbit alive? {rabbit in Animal.get_alive()}")  # False
    