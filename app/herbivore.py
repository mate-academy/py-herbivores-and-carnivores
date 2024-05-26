from app.animal import Animal


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
