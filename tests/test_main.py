import os

import pytest
import io

from contextlib import redirect_stdout

from app.main import Animal, Herbivore, Carnivore


def test_animal_class() -> None:
    assert hasattr(Animal, "alive"), "Animal class should have attribute 'alive'"


def test_animal_constructor() -> None:
    lion = Animal("Lion King")
    assert hasattr(lion, "name"), "Animal instance should have attribute 'name'"
    assert hasattr(lion, "health"), "Animal instance should have attribute 'health'"
    assert hasattr(lion, "hidden"), "Animal instance should have attribute 'hidden'"
    assert lion.name == "Lion King", (
        "'lion.name' should equal to 'Lion King' when "
        "'lion' created by 'Animal('Lion King')'"
    )
    assert lion.health == 100, (
        "'lion.health' should equal to 100 when "
        "'lion' created by 'Animal('Lion King')'"
    )
    assert lion.hidden is False, (
        "'lion.hidden' should equal to False when "
        "'lion' created by 'Animal('Lion King')'"
    )
    assert (
        len(Animal.alive) == 1
    ), "Constructor should add created animal to 'Animal.alive'"
    assert (
        Animal.alive[0].name == "Lion King"
    ), "Constructor should add created animal to 'Animal.alive'"


@pytest.mark.parametrize(
    "class_,method",
    [
        (Herbivore, "hide"),
        (Carnivore, "bite"),
    ],
)
def test_only_one_method_should_be_declared_in_each_of_children_classes(
    class_: type, method: str
) -> None:
    assert (
        Animal in class_.__bases__
    ), f"'{class_.__name__}' should be inherited from 'Animal'"
    assert (
        method in class_.__dict__
    ), f"Method '{method}' should be defined inside class '{class_.__name__}'"
    assert {"__init__", "__str__", "__repr__"}.intersection(
        class_.__dict__
    ) == set(), f"Magic methods should not be declared in {class_}"


def test_carnivore_bite_not_hidden() -> None:
    Animal.alive = []
    lion = Carnivore("King Lion")
    rabbit = Herbivore("Susan")
    lion.bite(rabbit)
    assert rabbit.health == 50, (
        "If initial health of rabbit equals 100 and rabbit is not hidden "
        "health should equal to 50 after bite."
    )


def test_carnivore_bite_hidden() -> None:
    Animal.alive = []
    lion = Carnivore("King Lion")
    rabbit = Herbivore("Susan")
    rabbit.hide()
    lion.bite(rabbit)
    assert rabbit.health == 100, "Carnivore cannot bite hidden herbivore"


def test_carnivore_bite_to_death() -> None:
    Animal.alive = []
    lion = Carnivore("King Lion")
    pantera = Carnivore("Bagira")
    rabbit = Herbivore("Susan")
    lion.bite(rabbit)
    pantera.bite(rabbit)
    assert len(Animal.alive) == 2, "It shouldn't be dead animals in Animals.alive"


def test_carnivore_bite_carnivore() -> None:
    lion = Carnivore("Simba")
    pantera = Carnivore("Bagire")
    lion.bite(pantera)
    assert pantera.health == 100


def test_herbivore_hide() -> None:
    Animal.alive = []
    rabbit = Herbivore("Susan")
    rabbit.hide()
    assert (
        rabbit.hidden is True
    ), "Method 'hide' should change animal attribute 'hidden'"
    rabbit.hide()
    assert (
        rabbit.hidden is False
    ), "Method 'hide' should change animal attribute 'hidden'"


def test_print_animal_alive() -> None:
    Animal.alive = []

    Carnivore("King Lion")
    Carnivore("Bagira")
    Herbivore("Susan")

    output_buffer = io.StringIO()

    with redirect_stdout(output_buffer):
        print(Animal.alive)

    out = output_buffer.getvalue()
    output = (
        "[{Name: King Lion, Health: 100, Hidden: False}, "
        "{Name: Bagira, Health: 100, Hidden: False}, "
        "{Name: Susan, Health: 100, Hidden: False}]\n"
    )
    assert out == output, (
        f"Output should equal to {output} when you print 'Animal.alive' with "
        f"three animals"
    )


def test_when_health_less_than_zero() -> None:
    Animal.alive = []
    lion = Carnivore("King Lion")
    rabbit = Herbivore("Susan", 25)
    lion.bite(rabbit)
    assert len(Animal.alive) == 1, "Herbivore should die if health less than zero"
    assert Animal.alive[0].name == "King Lion"


def test_unnecessary_comment() -> None:
    if os.path.exists(os.path.join(os.pardir, "app", "main.py")):
        main_path = os.path.join(os.pardir, "app", "main.py")
    else:
        main_path = os.path.join("app", "main.py")

    with open(main_path, "r") as main:
        main_content = main.read()

    assert "# write your code here" not in main_content, "Remove unnecessary comment"
