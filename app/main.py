# Classe base para todos os animais
class Animal:
    alive = []  # Lista de animais vivos

    def __init__(self, name: str) -> None:
        self.name: str = name          # Nome do animal
        self.health: int = 100         # Vida inicial
        self.hidden: bool = False      # Inicialmente não está escondido
        Animal.alive.append(self)      # Adiciona à lista de vivos

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def _die(self) -> None:
        # Remove da lista de vivos, se estiver nela
        if self in Animal.alive:
            Animal.alive.remove(self)


# Classe dos herbívoros, que herda de Animal
class Herbivore(Animal):
    def hide(self) -> None:
        # Alterna o estado de escondido
        self.hidden = not self.hidden


# Classe dos carnívoros, que herda de Animal
class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        # Só morde se for um herbívoro, visível e vivo
        if not isinstance(target, Herbivore):
            return

        if target.hidden or target.health <= 0:
            return

        target.health -= 50

        if target.health <= 0:
            target._die()
