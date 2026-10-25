from collections.abc import Generator

import pytest

from app.main import Animal


@pytest.fixture(autouse=True)
def reset_animal_alive() -> Generator[None, None, None]:
    Animal.alive.clear()
    yield
    Animal.alive.clear()
