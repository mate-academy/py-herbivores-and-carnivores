from __future__ import annotations
from app.anilmal.animal_base import Animal


class Herbivore(Animal):
    def hide(self) -> Animal:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True
        return self
