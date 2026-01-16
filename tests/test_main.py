from app.main import Animal, Herbivore, Carnivore


def test_animal_constructor():
    Animal.reset_alive()  # Очищаем список живых животных

    lion = Animal("Lion King")
    assert hasattr(lion, "name"), "Animal instance should have attribute 'name'"
    assert hasattr(lion, "health"), "Animal instance should have attribute 'health'"
    assert hasattr(lion, "hidden"), "Animal instance should have attribute 'hidden'"
    assert lion.name == "Lion King", "'lion.name' должно быть равно 'Lion King'"
    assert lion.health == 100, "'lion.health' должно быть равно 100"
    assert lion.hidden is False, "'lion.hidden' должно быть False"
    assert len(Animal.alive) == 1, "Конструктор должен добавлять созданное животное в 'Animal.alive'"


def test_when_health_less_than_zero():
    Animal.reset_alive()  # Очищаем список живых животных

    lion = Carnivore("King Lion")
    rabbit = Herbivore("Susan", 25)

    lion.bite(rabbit)
    assert rabbit.health == 0, "Здоровье кролика должно быть 0 после укуса"
    assert rabbit not in Animal.alive, "Мёртвые животные не должны быть в 'Animal.alive'"