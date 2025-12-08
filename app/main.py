class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Herbivore):
            if not target.hidden:
                target.health = target.health - 50

        if target.health <= 0:
            if target in Animal.alive:
                Animal.alive.remove(target)


if __name__ == "__main__":
    # 1. Test tworzenia Carnivore
    lion = Carnivore("Simba")
    print(f"Test 1: {len(Animal.alive) == 1}")

    # 2. Test Herbivore i chowania się
    rabbit = Herbivore("Susan")
    rabbit.hide()
    print(f"Test 2: {rabbit.hidden is True}")

    # 3. Test interakcji (Polowanie)
    lion = Carnivore("Lion King")
    rabbit = Herbivore("Susan")  # Nowy obiekt

    # Lew gryzie
    lion.bite(rabbit)
    print(f"Zdrowie po 1 ugryzieniu: {rabbit.health}")  # 50

    # Królik się chowa
    rabbit.hide()
    lion.bite(rabbit)
    print(f"Zdrowie (ukryty): {rabbit.health}")  # Nadal 50

    # Królik wychodzi
    rabbit.hide()
    lion.bite(rabbit)
    print(f"Zdrowie (śmiertelny): {rabbit.health}")  # 0

    # Czy królik zniknął?
    print(f"Martwy na liście? {rabbit in Animal.alive}")  # False

    print("-" * 20)
    print("OSTATECZNY WYGLĄD LISTY:")
    print(Animal.alive)
