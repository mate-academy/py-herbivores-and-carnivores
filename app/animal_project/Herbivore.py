from app.animal_project.Animal import Animal


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
