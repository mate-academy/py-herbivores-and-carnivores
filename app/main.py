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

    @classmethod
    def cleanup(cls) -> None:
        cls.alive = [
            animal for animal in cls.alive if animal.health > 0
        ]

    @classmethod
    def reset_alive(cls) -> None:
        cls.alive.clear()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: "Herbivore") -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            if prey.health <= 0:
                Animal.cleanup()


# Тест для конструктора

def test_animal_constructor() -> None:
    Animal.reset_alive()
    lion = Animal("Lion King")
    assert hasattr(lion, "name"), (
        "Animal instance should have attribute 'name'"
    )
    assert hasattr(lion, "health"), (
        "Animal instance should have attribute 'health'"
    )
    assert hasattr(lion, "hidden"), (
        "Animal instance should have attribute 'hidden'"
    )
    assert lion.name == "Lion King", (
        "'lion.name' should equal to 'Lion King' when "
        "'lion' created by 'Animal(\"Lion King\")'"
    )
    assert lion.health == 100, (
        "'lion.health' should equal to 100 when "
        "'lion' created by 'Animal(\"Lion King\")'"
    )
    assert lion.hidden is False, (
        "'lion.hidden' should equal to False when "
        "'lion' created by 'Animal(\"Lion King\")'"
    )
    assert len(Animal.alive) == 1, (
        "Constructor should add created animal to 'Animal.alive'"
    )


if __name__ == "__main__":
    # Пример использования
    lion = Carnivore("Simba")
    rabbit = Herbivore("Susan")
    print(Animal.alive)

    lion.bite(rabbit)
    print(rabbit.health)

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health)

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health)
    print(rabbit in Animal.alive)
