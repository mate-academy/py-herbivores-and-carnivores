from app.Animal import Animal


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True
