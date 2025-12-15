from app.animals.base.animal import Animal


class Herbivore(Animal):

    def hide(
        self
    ) -> None:
        self.hidden = not self.hidden
