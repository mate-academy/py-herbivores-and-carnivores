class Animal:
    # POPRAWKA 1: Adnotacja typu dla listy
    alive: list["Animal"] = []

    # POPRAWKA 2: Każdy parametr w nowej linii
    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
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
    # POPRAWKA 3: Tutaj też parametry w nowej linii
    def bite(
        self,
        target: Animal
    ) -> None:
        if isinstance(target, Herbivore):
            if not target.hidden:
                target.health = target.health - 50

        if target.health <= 0:
            if target in Animal.alive:
                Animal.alive.remove(target)


if __name__ == "__main__":
    # Twoje testy zostają bez zmian
    lion = Carnivore("Simba")
    print(f"Test 1: {len(Animal.alive) == 1}")

    rabbit = Herbivore("Susan")
    rabbit.hide()
    print(f"Test 2: {rabbit.hidden is True}")

    lion = Carnivore("Lion King")
    rabbit = Herbivore("Susan")

    lion.bite(rabbit)
    print(f"Zdrowie po 1 ugryzieniu: {rabbit.health}")

    rabbit.hide()
    lion.bite(rabbit)
    print(f"Zdrowie (ukryty): {rabbit.health}")

    rabbit.hide()
    lion.bite(rabbit)
    print(f"Zdrowie (śmiertelny): {rabbit.health}")

    print(f"Martwy na liście? {rabbit in Animal.alive}")

    print("-" * 20)
    print("OSTATECZNY WYGLĄD LISTY:")
    print(Animal.alive)