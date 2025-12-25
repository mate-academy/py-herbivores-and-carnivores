class Animal:
    alive = []

    def __init__(self, name: str, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def take_damage(self, damage) -> list:
        self.health -= damage
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self):
        return f'{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}'


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, food):
        if isinstance(food, Carnivore):
            print(
                f"{self.name} can not attacked {food.name} because it`s carnivore"
            )
            return

        if food.hidden:
            print(f'{self.name} can`t attacked {food.name} because it`s hide')
            return

        food.take_damage(50)
        return
