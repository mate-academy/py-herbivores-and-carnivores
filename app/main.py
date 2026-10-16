class Animal:
    # Atributo de classe para rastrear todos os animais vivos
    alive = []

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{self.name} ({self.health} HP)"


class Herbivore(Animal):
    def __init__(self, name: str, health: int = 100):
        super().__init__(name, health)
        self.hidden = False

    def hide(self):
        # Alterna o estado de ocultação
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal):
        # O carnívoro só pode morder se não for ele mesmo, se o alvo for um Herbívoro e se o herbívoro não estiver escondido
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                target.health = 0
                if target in Animal.alive:
                    Animal.alive.remove(target)
