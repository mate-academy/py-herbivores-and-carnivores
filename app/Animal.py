from __future__ import annotations


class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"
