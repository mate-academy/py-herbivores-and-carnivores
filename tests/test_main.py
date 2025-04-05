from app.main import Animal, Herbivore, Carnivore


def test_animal_class():
    Animal.alive.clear()

    lion = Carnivore("Simba")
    assert len(Animal.alive) == 1
    assert isinstance(Animal.alive[0], Carnivore)


def test_animal_constructor():
    Animal.alive.clear()

    rabbit = Herbivore("Coelho")
    assert rabbit.name == "Coelho"
    assert rabbit.health == 100
    assert not rabbit.hidden
    assert rabbit in Animal.alive


def test_carnivore_bite_to_death():
    Animal.alive.clear()

    rabbit = Herbivore("Pernalonga")
    lion = Carnivore("Simba")

    rabbit.hide()  # Esconde, não pode ser mordido
    lion.bite(rabbit)
    assert rabbit.health == 100

    rabbit.hide()  # Mostra
    lion.bite(rabbit)
    assert rabbit.health == 50  # Corrigido: perdeu 50

    rabbit.hide()  # Esconde
    lion.bite(rabbit)
    assert rabbit.health == 50  # Não foi mordido

    rabbit.hide()  # Mostra
    lion.bite(rabbit)
    assert rabbit.health == 0  # Morreu
    assert rabbit not in Animal.alive
